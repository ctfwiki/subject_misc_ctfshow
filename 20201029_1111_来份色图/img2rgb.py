from PIL import Image
from math import sqrt

def img2setu(source,dist):
    bytes = open(source,"rb").read()
    length = len(bytes)//3
    height = int(sqrt(length)*0.618)
    width = int((length-1)/height)+1
    print(width,height,width*height*3-len(bytes))
    bytes += b'\xff'*(width*height*3-len(bytes))

    it = iter(bytes)
    img = Image.new('RGB', (width, height))
    for y in range(height):
        for x in range(width):
            img.putpixel((x,y),(next(it),next(it),next(it)))
    img.save(dist)

def setu2img(source,dist):
    f = open(dist,"wb")
    img = Image.open(source)
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r,g,b = img.getpixel((x,y))
            f.write(r.to_bytes(1, 'little'))
            f.write(g.to_bytes(1, 'little'))
            f.write(b.to_bytes(1, 'little'))
    f.close()

if __name__ == '__main__':
    # img2setu("1.png", "setu1.png")
    # img2setu("3.png", "setu3.png")
    setu2img("setu1.png", "ori1.png")
    setu2img("setu3.png","ori3.png")
