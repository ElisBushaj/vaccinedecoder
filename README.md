# vaccinedecoder
Python script to decode the EU Covid-19 vaccine certificate.
This script takes an image with a QR code of a vaccine certificate as the parameter and will show the certificate's content.

How these certificates are encoded:

* The QR code encodes a string starting with "HC1:".
* The string following "HC1:" is base45 encoded.
* Decoding the base45 leads to zlib-compressed data.
* Decompression leads to a CBOR Web Token structure.

## setup

You will need the python pillow, pyzbar, zlip, cose, cbor2 and base45 packages.

You can install them via your distribution or via pip:

```
pip install base45 cbor2 pillow pyzbar cose zlip
```
