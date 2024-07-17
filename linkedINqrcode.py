import qrcode



# Data to be encoded in the QR code
data = "https://www.linkedin.com/in/shiwangi-singh-kushwaha"

# Generate the QR code
img = qrcode.make(data)

# Save the generated QR code to a file
img.save("shiwangi_linkedIN.png")
