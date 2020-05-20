# https://www.jianshu.com/p/dda608dbaca5
import qrcode

def gen_qrcode(data,savepath,ecorrect,bsize=25,border=2,fcolor="black",bcolor="white"):
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

# 25*25
def gen_main_qrcode(data):
    # rgb(0,0,0)
    # black
    # #000000
    gen_qrcode(data,savepath="qrcode/main_qrcode.png",ecorrect=qrcode.constants.ERROR_CORRECT_L)

def gen_data_qrcode():
    i = 0
    f = open("data.txt",encoding='utf-8')
    for data in f.readlines():
        data = data[:-1]
        if len(data) >= 5:# data长度生成二维码是25*25
            gen_qrcode(data,savepath=("qrcode/%s.png"%i),ecorrect=qrcode.constants.ERROR_CORRECT_H, bsize=1, border=0)
            i += 1

def gen_flag_qrcode(flag):
    gen_qrcode(flag, savepath="qrcode/flag.png",ecorrect=qrcode.constants.ERROR_CORRECT_L, bsize=1, border=0)

# gen_main_qrcode("这里只有二维码")
# gen_data_qrcode() # 天tiān 地dì
gen_flag_qrcode("flag{luck_is_power}")# "flag{luck_is_power}"
