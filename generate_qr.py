import qrcode

def generate_static_qr(url="http://10.10.83.46:5000"):
    img = qrcode.make(url)
    img.save("static/qr_image.png")
    print("QR Code saved as static/qr_image.png")

if __name__ == "__main__":
    generate_static_qr()