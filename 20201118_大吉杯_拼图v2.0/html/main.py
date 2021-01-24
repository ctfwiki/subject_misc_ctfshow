import os, shutil, random, hashlib
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder='./templates',
    static_folder='./static',
    static_url_path='/static'
)

block_size = 15

@app.route('/')
def index():
    global block_size
    return render_template('index.html',width=int(630/block_size), height=int(630/block_size))

def draw_flag(flag):
    # 读取图片
    base = Image.open('origin.jpg').convert('RGBA')
    # 创建空白图片
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    # 读取字体文件
    fnt = ImageFont.truetype('gjmt.ttf', 100)
    # get a drawing context
    d = ImageDraw.Draw(txt)
    # 写字，半透明
    d.text((25,10), flag[:7], font=fnt, fill=(255,255,255,128))
    d.text((80,110), flag[7:14], font=fnt, fill=(255,255,255,128))
    d.text((135,210), flag[14:21], font=fnt, fill=(255,255,255,128))
    d.text((190,310), flag[21:28], font=fnt, fill=(255,255,255,128))
    d.text((245,410), flag[28:35], font=fnt, fill=(255,255,255,128))
    d.text((300,510), flag[35:], font=fnt, fill=(255,255,255,128))
    # 写字，不透明
    # d.text((10,60), "World", font=fnt, fill=(255,255,255,255))
    # fillcolor = "#ff0000"  #字体颜色
    # d.text((base.size[0]-20,10), "4", font=fnt, fill=fillcolor)
    return Image.alpha_composite(base, txt)

def split_save(img,width_total,height_total):
    dirpath = os.path.join(os.getcwd(),"static/img/blocks")
    print("dirpath:",dirpath)
    # 清空文件夹
    shutil.rmtree(dirpath)
    os.mkdir(dirpath)
    bwidth,bheight = img.size
    bwidth = bwidth / width_total
    bheight = bheight / height_total
    block_list = []
    for y in range(height_total):
        for x in range(width_total):
            block = img.crop((bwidth*x, bheight*y, bwidth*(x+1), bheight*(y+1)))
            rota = random.randint(0, 3) # 随机旋转
            if rota == 1:
                block = block.transpose(Image.ROTATE_90)
            elif rota == 2:
                block = block.transpose(Image.ROTATE_180)
            elif rota == 3:
                block = block.transpose(Image.ROTATE_270)
            file_name = hashlib.md5(block.tobytes()).hexdigest()[8:24]
            block_list.append(file_name)
            block.save("static/img/blocks/%s.png" % file_name)
    f = open(os.path.join(os.getcwd(),"static/js/data.js"), "w")
    f.write("var block_data = [")
    for i in range(len(block_list)):
        name = random.choice(block_list)
        block_list.remove(name)
        f.write("'" + name + "',")
    f.write("];")

if __name__ == '__main__':
    demo_flag = os.environ["FLAG"]
    # demo_flag = "flag{10ff6f14-a974-4e53-9eed-0983d5be94ed}"

    img = draw_flag(demo_flag)
    split_save(img,block_size,block_size)
    app.run(debug=False, host='0.0.0.0', port=3333)