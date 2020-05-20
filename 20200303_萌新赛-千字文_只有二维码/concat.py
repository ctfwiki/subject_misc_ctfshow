# https://blog.csdn.net/Zhipeng_Hou/article/details/83381133
import os,random
from PIL import Image

base_dir = "qrcode/"
def walkfile():
    qrcodes = []
    for parent, dirnames, filenames in os.walk(base_dir,  followlinks=True):
        for filename in filenames:
            if filename != "main_qrcode.png" and filename != "flag.png":
                qrcodes.append(filename)
    # print(len(qrcodes))
    return qrcodes

def random_int(max,min = 0):
    return random.randint(min,max)# 0 ≤ x ≤ 5


def convert_img(img_file,isWhite):
    black = (0,0,0)
    white = (255,255,255)
    if isWhite:
        black = (254,254,254)
    else:
        white = (1,1,1)
    img = Image.open(img_file)
    width,height = img.size
    img_new = Image.new('RGB', (width, height))
    for w in range(width):
        for h in range(height):
            color = img.getpixel((w,h))
            if color == 0:
                img_new.putpixel((w,h),black)
            else:
                img_new.putpixel((w,h),white)
    return img_new


qlist = walkfile()

img = Image.open("qrcode/main_qrcode.png")
width,height = img.size # 676*676
# print(width,height)
img_concat = Image.new('RGB', (width, height),color=(255,255,255))

box_width = int(width/25)
box_height = int(height/25)
flag_w = random_int(min = 2,max = box_width-3)
flag_h = random_int(min = 2,max = box_height-3)
print("flag position: ", flag_w, flag_h)

for w in range(2,box_width-2):
    for h in range(2,box_height-2):
        # print(w,h)
        if w == flag_w and h == flag_h:# 添加flag.png
            color = img.getpixel(((w*25+13), (h*25+13)))
            print("flag color: ",color)
            img_sm = convert_img("qrcode/flag.png",color > 127)
            # 拼接小二维码到大二维码
            img_concat.paste(img_sm,(w*25,h*25))
        else:
            # 取随机二维码
            ran = random_int(len(qlist)-1)
            fn = qlist.pop(ran)
            # 读取小二维码
            color = img.getpixel(((w*25+13), (h*25+13)))
            img_sm = convert_img("qrcode/"+fn,color > 127)
            # 拼接小二维码到大二维码
            img_concat.paste(img_sm,(w*25,h*25))

img_concat.show()
img_concat.save("千字文.png")
