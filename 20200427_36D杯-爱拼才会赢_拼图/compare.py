from PIL import Image
import hashlib

width = 23
height = 13

# 读原图
full_color = []
origin_img = Image.open("origin_img.jpg")
for y in range(height):
    for x in range(width):
        if y == height-1 and x == width-1:
            break
        # 200*150
        color_simple = []
        sx = 200 * x
        sy = 150 * y
        # 6个采样点
        color_simple.append(origin_img.getpixel((sx+50,sy+50)))
        color_simple.append(origin_img.getpixel((sx+100,sy+50)))
        color_simple.append(origin_img.getpixel((sx+150,sy+50)))
        color_simple.append(origin_img.getpixel((sx+50,sy+100)))
        color_simple.append(origin_img.getpixel((sx+100,sy+100)))
        color_simple.append(origin_img.getpixel((sx+150,sy+100)))
        full_color.append(color_simple)

# 读碎片
block_color = {}
for i in "0123456789abcdefg":
    for j in "0123456789abcdefgh":
        name = i + j
        if name == "gb":
            break
        if name != "00":
            block = Image.open("data/%s.jpg" % name)
            block_color[name] = []
            block_color[name].append(block.getpixel((50,50)))
            block_color[name].append(block.getpixel((100,50)))
            block_color[name].append(block.getpixel((150,50)))
            block_color[name].append(block.getpixel((50,100)))
            block_color[name].append(block.getpixel((100,100)))
            block_color[name].append(block.getpixel((150,100)))

# print(len(block_color))
# print(len(full_color))

puzdict = {}
for k,v in block_color.items():# 每个碎片
    idx = 0
    max = -1
    for b in range(len(full_color)):# 原图中每块
        if b not in puzdict:
            cha = 0
            for i in range(6):
                cha += abs(full_color[b][i][0] - v[i][0])
                cha += abs(full_color[b][i][1] - v[i][1])
                cha += abs(full_color[b][i][2] - v[i][2])
            if max == -1 or cha < max:
                max = cha
                idx = b
    puzdict[idx] = k
    print("find key: %s,idx: %s,len: %s"%(k,idx,len(full_color)))

print(len(puzdict))
puzstr = ""
for i in range(len(puzdict)):
    puzstr += puzdict[i]

print("puzstr: "+puzstr)
# be2b50b9468fae9a9dd7990d51270bcafccc6d34c2e1aeb7308d0f99634ca2d0
# sha256 = hashlib.sha256(puzstr.encode()).hexdigest()
# md5 = hashlib.md5(puzstr.encode()).hexdigest()
# print("sha256: "+sha256)
# print("md5: "+md5)
