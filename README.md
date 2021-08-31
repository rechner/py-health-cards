# py-health-cards

A python library for decoding the [SMART health card standard](https://smarthealth.cards/), used for documenting
COVID-19 vaccination history or test results as a QR code as a JWT in a verifiable manner, and is being issued by
several localities (e.g. California, Quebec).


## Example

```python
record = "shc:/..."
from healthcards import parser
jws_str = parser.decode_qr_to_jws(record)
jws = parser.JWS(jws_str)
jws.verified
jws.as_dict()
```
