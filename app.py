try:
    import barcode
    import qrcode
    from barcode.writer import ImageWriter
    import cv2
    import numpy as np
    from pyzbar.pyzbar import decode
except Exception as e:
    print(f"An importation error occured")


def createQRCode():
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    while True:
        data = input(
            "Enter the text or link you want to convert to a QR code. ")
        if(len(data) > 0):
            break
        else:
            print("Enter a vaild string")
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qr.png")


def createBarCode():
    hr = barcode.get_barcode_class("code39")
    while True:
        userInput = input("Enter the test your want to encode. ")
        if(len(userInput) > 0):
            break
        else:
            print("Enter an valid string")
    Hr = hr(userInput, writer=ImageWriter())
    br = Hr.save("barcode")


def readQrCode():
    print("Move the QR Code to a same directry of the app.py")
    imageName = input("Now Enter the name of the image with it extension")
    img = cv2.imread(imageName)
    for qrcode_ in decode(img):
        decodedCode = qrcode_.data.decode("utf-8")
        print(decodedCode)


def readBarCode():
    print("Move The QR Code to a same directry of the app.py")
    imageName = input("Now Enter the name of the image with it extension")
    img = cv2.imread(imageName)
    for barcode_ in decode(img):
        decodedCode = barcode_.data.decode("utf-8")
        print(decodedCode)


def application():
    ##Application Interface##
    print("Welcome to the QR_App here you can create QR code, Bar Code, Scan bar and QR code for details")
    print("Enter cb to create bar code ")
    print("Enter cq to create QR code ")
    print("Enter rq to read QR plainly")
    print("Enter rb to read bar code ")
    user_choice = input()
    if(user_choice == "cq"):
        createQRCode()
    elif(user_choice == "cb"):
        createBarCode()
    elif(user_choice == "rq"):
        readQrCode()
    elif(user_choice == "rb"):
        readBarCode()


application()
