# QR-Code-Generator 
How to Create QR Code Generator in Python on VS Code

Install the qrcode library: First, ensure that you have the qrcode library installed. You can install it using pip if you haven't already:
"pip install qrcode[pil]"

Write the Python script: Open a new Python file in VSCode and write the following script to create and save the QR code

let's break down the code step by step to understand what each part does:

Import Libraries

import qrcode
from PIL import Image
qrcode: This is the library used to generate QR codes.
from PIL import Image: This imports the Image class from the Python Imaging Library (PIL), although it's not explicitly used in the code.
Create a QRCode Object

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr = qrcode.QRCode(...): This creates a QRCode object with specific settings:
version=1: This parameter controls the size of the QR code. Version 1 is a 21x21 matrix. Higher versions create larger QR codes that can hold more data.
error_correction=qrcode.constants.ERROR_CORRECT_H: This sets the error correction level to 'H' (High), which allows the QR code to be read even if up to 30% of it is damaged or obscured.
box_size=10: This sets the size of each box (or pixel) in the QR code to 10x10 pixels.
border=4: This sets the border width (minimum value is 4) around the QR code.

Add Data to the QRCode

qr.add_data("https://github.com/SSK-0809")
qr.add_data("https://github.com/SSK-0809"): This adds the data (in this case, a URL) that you want to encode in the QR code.

Generate the QR Code

qr.make(fit=True)
qr.make(fit=True): This generates the QR code. The fit=True parameter ensures that the QR code size is adjusted to fit the data provided.

Create the QR Code Image

img = qr.make_image(fill_color="green", back_color="white")
img = qr.make_image(fill_color="green", back_color="white"): This creates an image of the QR code with the specified colors:
fill_color="green": This sets the color of the QR code modules (the black squares) to green.
back_color="white": This sets the background color of the QR code to white.

Save the QR Code Image

img.save("shiwangi_github.png")
img.save("shiwangi_github.png"): This saves the generated QR code image to a file named shiwangi_github.png.

 Code Summary

import qrcode
from PIL import Image

# Create a QR code object with specified parameters
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data("https://github.com/SSK-0809")

# Generate the QR code
qr.make(fit=True)

# Create an image of the QR code with specified colors
img = qr.make_image(fill_color="green", back_color="white")

# Save the image to a file
img.save("shiwangi_github.png")
This script generates a QR code for the URL https://github.com/SSK-0809, creates an image of the QR code with green modules and a white background, and saves the image as shiwangi_github.png.






