from PIL import Image
import qrcode

def gen_qrcode(data,savepath,ecorrect,bsize=1,border=1,fcolor="black",bcolor="white"):
    # 实例化二维码生成类
    qr = qrcode.QRCode(
        version=1,
        error_correction=ecorrect,
        box_size=bsize,
        border=border
    )
    # 设置二维码数据
    qr.add_data(data=data)

    # 启用二维码颜色设置
    qr.make(fit=True)
    img = qr.make_image(fill_color=fcolor, back_color=bcolor)

    # 显示二维码
    # img.show()
    img.save(savepath)

flag = "flag{bin_2_qrcode}"
qrfile = "qrcode.png"
gen_qrcode(flag,savepath=qrfile,ecorrect=qrcode.constants.ERROR_CORRECT_L)
f = open("qrcode.txt",'w')
img = Image.open(qrfile)
width,height = img.size
for w in range(1,width-1):
    for h in range(1,height-1):
        color = img.getpixel((w,h))
        x = -1
        if color == 0:
            x = 1
        elif color == 255:
            x = 0
        f.write(str(x))
f.close()
