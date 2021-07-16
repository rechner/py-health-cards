import base64
import json
import logging
import re
import urllib.request
import zlib
from typing import Dict, Optional, Union

from jwcrypto import jws
from jwcrypto.jwk import JWKSet

CHUNKING_RE = re.compile(r"^shc:/(\d*)/(\d*)/(\d*)$")
logger = logging.getLogger(__name__)


class BaseError(Exception):
    pass


class ParserError(BaseError):
    pass


class VerificationError(BaseError):
    pass


class JWS(object):
    def __init__(self, jws: str):
        self.jws = jws
        self.header = None
        self.payload = None
        self.signature = None
        self.issuer = None
        self.verified = False
        self._decode_jws()
        self._validate_jwt()

    def _decode_jws(self) -> None:
        def decode_base64(data: str) -> bytes:
            missing_padding = len(data) % 4
            if missing_padding:
                data += "=" * (4 - missing_padding)
            return base64.urlsafe_b64decode(data)

        jws_parts = list(map(decode_base64, self.jws.split(".")))
        if len(jws_parts) != 3:
            raise ParserError(
                f"JWS token was expected to have 3 parts, {len(jws_parts)} parts found."
            )

        logger.debug(f"JWS decoded to: {jws_parts}")
        self.header = json.loads(jws_parts[0])

        payload: bytes = jws_parts[1]
        if "zip" in self.header:
            payload: bytes = zlib.decompress(jws_parts[1], wbits=-15)
        self.payload = json.loads(payload)

        try:
            self.issuer = self.payload["iss"]
        except KeyError:
            raise ParserError("Payload is missing required field 'iss'")

        self.signature: bytes = jws_parts[2]

    def _validate_jwt(self):
        key_url = f"{self.issuer}/.well-known/jwks.json"
        keyset = JWKSet()
        with urllib.request.urlopen(key_url) as response:
            data = response.read()
            keyset.import_keyset(data)
            logger.debug(f"Fetching JWK from issuer: {key_url}")
            key = keyset.get_key(self.header["kid"])
            logger.debug(f"Using key {key} from keyset.")
            jws_token = jws.JWS()
            jws_token.deserialize(self.jws)

            # FIXME: Specify expected algorithms or at least prevent alg:none
            jws_token.verify(key)
            self.verified = jws_token.is_valid
        return self.verified

    def as_dict(self):
        result = {
            "header": self.header,
            "payload": self.payload,
            "verification": {"verified": self.verified},
        }
        return result


def decode_qr_to_jws(encoded_list: Union[list, str]) -> str:
    """
    Parses a chunked, numerically-encoded SMART Health Card as formatted for QR code
    representations.

    For more details about the chunking scheme, see https://spec.smarthealth.cards/#chunking
    """
    if type(encoded_list) == str:
        encoded_list = [encoded_list]

    reconstructed: Dict[int, str] = {}
    chunks_total_history: list(int) = []
    for encoded in encoded_list:
        encoded: str = encoded.lower()
        if not encoded.startswith("shc:/"):
            raise ParserError("Schema indicator not found, not a valid SHC!")

        chunking_match: Optional[re.match] = CHUNKING_RE.match(encoded)
        if chunking_match:
            chunk_count = int(chunking_match.group(1))
            chunks_total = int(chunking_match.group(2))
            chunk_body = chunking_match.group(3)
            logger.debug(
                f"Got chunk {chunk_count} of {chunks_total}: {chunk_body[:10]}..."
            )

        else:
            chunk_count = 1
            chunks_total = 1
            chunk_body = encoded.split("/")[-1]

        if len(chunk_body) % 2 != 0:
            raise ParserError("Chunk body length must be even (2 digits per character)")

        chunks_total_history.append(chunks_total)

        # Decode 2-digit integers into bytes to reconstruct the base64 string:
        parts: Optional[re.match] = re.findall("..", chunk_body)
        jws_part: str = "".join([chr(int(p) + 45) for p in parts])
        reconstructed[chunk_count] = jws_part

    if chunks_total_history.count(chunks_total_history[0]) != len(chunks_total_history):
        raise ParserError(
            f"An SHC chunk provided did not match the expected number of chunks {chunks_total_history[0]}"
        )
    if list(reconstructed.keys()) != list(range(1, chunks_total + 1)):
        raise ParserError(
            "An expected chunk required to reconstruct this SHC is missing"
        )

    jws = "".join(reconstructed.values())
    logger.debug(f"Reconstructed JWS from {chunks_total_history[0]} chunks: {jws}")
    return jws


def setup_logging() -> None:
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
