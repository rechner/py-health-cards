from unittest import TestCase, mock
from unittest.mock import Mock

from healthcards import parser
from .test_data import *


class TestDecodeQR(TestCase):
    def test_single_decode_qr_to_jws(self):
        jws = parser.decode_qr_to_jws(SINGLE_SHC)
        self.assertEqual(jws, SINGLE_SHC_JWS)

    def test_double_decode_qr_to_jws(self):
        jws = parser.decode_qr_to_jws(DOUBLE_SHC)
        self.assertEqual(jws, SINGLE_SHC_JWS)

    def test_odd_length_decode_qr_to_jws(self):
        test_payload = SINGLE_SHC[:-1]
        self.assertRaises(parser.ParserError, parser.decode_qr_to_jws, test_payload)

    def test_invalid_schema_shc_decode_qr_to_jws(self):
        test_payload = "definitely not an SHC"
        self.assertRaises(parser.ParserError, parser.decode_qr_to_jws, test_payload)

    def test_invalid_double_shc_decode_qr_to_jws(self):
        self.assertRaises(parser.ParserError, parser.decode_qr_to_jws, INVALID_DOUBLE_SHC)

    @mock.patch('urllib.request.urlopen')
    def test_decode_jws(self, mock_urlopen):
        m = Mock()
        rm = Mock()
        rm.read.return_value = EXAMPLE_KEYS_RESPONSE
        m.__enter__ = Mock(return_value=rm)
        m.__exit__ = Mock()
        mock_urlopen.return_value = m

        parser.setup_logging()
        jws_str = parser.decode_qr_to_jws(SINGLE_SHC)
        self.assertEqual(jws_str, SINGLE_SHC_JWS)
        jws = parser.JWS(jws_str)
        self.assertTrue(jws.verified)