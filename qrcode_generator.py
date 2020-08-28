import qrcode
import glob
import os

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

def getLink():
    URL = input("Enter the link which needs to get translated to QR: ")
    return URL

if __name__ == "__main__":
    qr_dir = os.path.join(os.getcwd(), "QR Codes")
    if not os.path.exists(qr_dir):
        os.mkdir(qr_dir)    
    URL = getLink()
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    imgList = glob.glob("*.png")
    if len(imgList) == 0:
        img.save('QR Codes/qrcode.png')
    else:
        imgNumber = len(imgList)
        img.save(f'QR Codes/qrcode_{imgNumber}.png')