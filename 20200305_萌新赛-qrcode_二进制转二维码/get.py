from pyzbar import pyzbar
from PIL import Image


def decode_qr_code(img):
    txt = pyzbar.decode(img, symbols=[pyzbar.ZBarSymbol.QRCODE])
    if len(txt):
        return txt[0].data.decode("utf-8")
    else:
        return "decode fail"

qrcode = Image.new('RGB', (27, 27),color=(255,255,255))
f = open("qrcode.txt")
txt = f.read()
x=y=1
for i in txt:
    if i == "1":
        color = 0
    else:
        color = 255
    qrcode.putpixel((x,y), (color,color,color))
    x += 1
    if x > 25:
        x = 1
        y += 1
# qrcode.show()
print(decode_qr_code(qrcode))
