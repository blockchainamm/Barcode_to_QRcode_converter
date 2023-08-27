# Barcode to QR code converter

This python script can read barcode from a given image and generate a QR code from the decoded barcode data.

The pyzbar library in python is used to decode the rectangles in the barcode.

The pyzbar can return 3 fields based on the barcode object:

- Type: There are several kinds of barcodes available. Which are differentiated by unique code names like CODE-128, Code-11, CODE-39 etc. 
- Data: This is data that is embedded inside the barcode. This data is of various kinds ( alphanumerical, numerical, binary, etc..) depending on the type of barcode.
- Location: This is the collection of points that are located in the code. For barcodes, these points are starting and ending line boundaries.

For a given image such as,

![barcodeimage_small](https://github.com/blockchainamm/blockchainamm/assets/82846751/be9db3dc-aa28-4abe-ad82-3db73c38eeb7)

- The barcode data is JJD014600011157960726
- The barcode unique code is of type CODE128

The QR code generated based on the decoded barcode data from the input file is shown below,

<img width="126" alt="qrcode_small" src="https://github.com/blockchainamm/blockchainamm/assets/82846751/3d5ab042-7974-4b7e-bc22-c624832bb265">
