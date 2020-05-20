import os
import zipfile
import random

# https://blog.csdn.net/zerothy/article/details/102908010
miniZip_path = "./lib/minizip.exe"

# 加密压缩
def createEncryptedFile(password,zipfile_path,source_path):
    cmd = '{} -o -1 -p "{}" "{}" "{}"'.format(miniZip_path,password,zipfile_path,source_path)
    os.system(cmd)
    print(cmd)
    os.remove(source_path)

# 遍历目录中文件
def get_filelist(dir):
    for home, dirs, files in os.walk(dir):
        return files

# 取随机数a <= n <= b
def rand(a,b):
    return random.randint(a,b)

# 把zip文件附加到jpg图片末尾另存为i.jpg
def copyZip2Jpg(fzip,fjpg,fout):
    f1=open(fzip, 'rb')
    f2=open("./movies/"+fjpg, 'rb')
    f3=open("%s.jpg"%fout, 'wb')
    f3.write(f2.read())
    f3.write(f1.read())
    f3.close()
    f1.close()
    f2.close()

if __name__ == '__main__':
    # 读取所有图片列表[name].replace("斜斜斜线","/")
    filelist=get_filelist("./movies/")
    # print(len(filelist),filelist[1])
    i=333
    # 随机取出图片文件名
    fn=filelist.pop(rand(0,len(filelist)-1))
    pwd=fn[:fn.rindex(".")].replace("斜斜斜线","/")
    # 加密flag文件
    createEncryptedFile(pwd,"123.zip","girl.txt")
    # 压缩包附加到图片另存为i.jpg
    copyZip2Jpg("123.zip",fn,i)
    i-=1
    while i>=0:
        # 随机取出图片文件名
        fn=filelist.pop(rand(0,len(filelist)-1))
        # print(len(filelist),i,fn)
        pwd=fn[:fn.rindex(".")].replace("斜斜斜线","/")
        # 加密上一个图片
        createEncryptedFile(pwd,"123.zip","%s.jpg"%(i+1))
        # 压缩包附加到图片另存为i.jpg
        copyZip2Jpg("123.zip",fn,i)
        i-=1

    # createEncryptedFile("肖申克的救赎","123.zip","girl.txt")
