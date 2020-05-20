import qrcode
from PIL import Image

def gen_qrcode(data,bsize=25,border=1,fcolor="black",bcolor="white"):
    # 实例化二维码生成类
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=bsize,
        border=border
    )
    # 设置二维码数据
    qr.add_data(data=data)

    # 启用二维码颜色设置
    qr.make(fit=True)
    img = qr.make_image(fill_color=fcolor, back_color=bcolor)

    # 显示二维码
    img.show()
    img.save("qrcode.png")

def qr2bin():
    bin=""
    img = Image.open("qrcode.png")
    width,height = img.size
    img_new = Image.new('RGB', (width, height))
    for y in range(29):
        for x in range(29):
            color = img.getpixel((x*25+12,y*25+12))
            if color == 0:
                bin+="1"
            else:
                bin+="0"
    print(bin)

gen_qrcode("flag{TgCannotGetHouse}")
# qr2bin()
