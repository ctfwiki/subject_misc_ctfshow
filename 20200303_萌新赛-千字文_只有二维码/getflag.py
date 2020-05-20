from pyzbar import pyzbar
from PIL import Image

def decode_qr_code(img):
    txt = pyzbar.decode(img, symbols=[pyzbar.ZBarSymbol.QRCODE])
    if len(txt):
        return txt[0].data.decode("utf-8")
    else:
        return ""

img = Image.open("千字文.png")
for w in range(2,27):
    for h in range(2,27):
        qrcode = Image.new('RGB', (27, 27),color=(255,255,255))
        wq = w*25
        hq = h*25
        for x in range(wq,wq+25):
            for y in range(hq,hq+25):
                r,g,b = img.getpixel((x,y))
                color = b
                if color == 254:
                    color = 0
                elif color == 1:
                    color = 255
                qrcode.putpixel((x-wq+1,y-hq+1), (color,color,color))
        # qrcode.show()
        txt = decode_qr_code(qrcode)
        if "flag" in txt:
            print(w,h,txt)
