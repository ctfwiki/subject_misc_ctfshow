import hashlib
from PIL import Image

charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}"

hash = []

for i in range(10):
    bin = ""
    img = Image.open("data/%s.png"%i)
    for x in range(2,-1,-1):
        for y in range(5):
            r,g,b,a = img.getpixel(((x*2+2)*35,(y*2+2)*35))
            bin += "1" if r == 240 else "0"
    print(bin)
    hash.append(bin)

dic = {}

for c1 in charset:
    for c2 in charset:
        s = c1 + c2
        h = hashlib.md5(s.encode()).hexdigest()
        bin = ""
        for c in h[:15]:
            bin += "1" if int(c,16) % 2 == 1 else "0"
        if bin in hash:
            dic[hash.index(bin)] = s
            # print(s)

for i in range(10):
    print(dic[i],end="")
