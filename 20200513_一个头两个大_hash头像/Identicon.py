import re,math
import hashlib
from PIL import Image,ImageDraw
import HSL

# https://avatars2.githubusercontent.com/u/62230282?s=400&v=5
# https://cdn.v2ex.com/gravatar/8a426e1ecdc693b9c9e528b1465cefad?s=73&d=retro

# 62230282		216	41	80		789acd		85014617f14d6f9 131fb8f8d3995f391
# 62071247		97	40	86		a4db83		764eca8765bfa13 1037d372c34567e52
# 61263923		182	32	88		99dee1		49ffc41ce302043 80e584364181c880d

defaults = {
    "background": (240, 240, 240, 255),
    "margin":     1/12,
    "size":       420,
    "saturation": 0.46,
    "brightness": 0.637
}

def gen_icon(text):
    hash = hashlib.md5(text.encode()).hexdigest()
    # print(text,hash)
    size       = defaults["size"]
    baseMargin = math.floor(size * defaults["margin"])
    cell       = math.floor((size - (baseMargin * 2)) / 5)
    margin     = math.floor((size - cell * 5) / 2)

    hue = int(hash[-7:],16) / 0xfffffff
    foreground = HSL.hsl2rgb([hue, defaults["saturation"], defaults["brightness"]])
    icon = Image.new(mode="RGBA",size=(size,size),color=defaults["background"])
    draw = ImageDraw.Draw(icon)
    for i in range(15):
        if int(hash[i],16) % 2 == 0:
            if i < 5:
                draw.rectangle((2 * cell + margin,i * cell + margin,3 * cell + margin,(i + 1) * cell + margin),fill=foreground)
            elif i < 10:
                draw.rectangle((1 * cell + margin,(i - 5) * cell + margin,2 * cell + margin,(i - 4) * cell + margin),fill=foreground)
                draw.rectangle((3 * cell + margin,(i - 5) * cell + margin,4 * cell + margin,(i - 4) * cell + margin),fill=foreground)
            else:
                draw.rectangle((0 * cell + margin,(i - 10) * cell + margin,1 * cell + margin,(i - 9) * cell + margin),fill=foreground)
                draw.rectangle((4 * cell + margin,(i - 10) * cell + margin,5 * cell + margin,(i - 9) * cell + margin),fill=foreground)
    icon.save("gen/"+text+".png")


flag = "flag{ZhEnDeShAnGtOu}"
for txt in re.findall(r'.{2}',flag):
    gen_icon(txt)
# gen_icon("62230282")
