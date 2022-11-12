import qrcode
text = input("Enter the text: ")
address = input("Enter the address: ")
qr = qrcode.make(text  , address)
qr.save("Qrcode.jpg")