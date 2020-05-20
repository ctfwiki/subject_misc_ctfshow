import zipfile,os
import hashlib

# 遍历目录中文件
def get_filelist(dir):
    for home, dirs, files in os.walk(dir):
        return files

def get_file_md5(file_path):
    print("计算文件hash："+file_path)
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).upper()

def split(i):
    img = "./m/%s.jpg"%i
    print("分离图片："+img)
    iFile = open(img,'rb')
    iBytes = iFile.read()
    iFile.close()

    index = iBytes.find(b"\xff\xd9\x50\x4B\x03\x04")+2
    jpgBytes = iBytes[:index]
    fjpg = open("./m/%s.jpg"%(i+1),'wb')
    fjpg.write(jpgBytes)
    fjpg.close()

    zipBytes = iBytes[index:]
    fzip = open("./m/123.zip",'wb')
    fzip.write(zipBytes)
    fzip.close()

    if i%20!=0:
        os.remove(img)

if __name__ == '__main__':
    # 读取所有图片文件名
    filelist = get_filelist("./movies/")
    # 计算图片hash
    print("初始化密码字典...")
    dict = {}
    for fn in filelist:
        dict[get_file_md5("./movies/"+fn)] = fn[:fn.rindex(".")].replace("斜斜斜线","/")
    print("开始解压...")
    i=48
    while True:
        # 分离图片和压缩包
        split(i)
        # 计算图片hash值获得解压密码
        password = dict.pop(get_file_md5("./m/%s.jpg"%(i+1))).replace("斜斜斜线","/")
        print("开始解压文件，密码："+password)
        # 解压出文件
        zFile = zipfile.ZipFile("./m/123.zip", "r")
        for fileM in zFile.namelist():
            zFile.extract(fileM, "./m/", pwd=password.encode("gbk"))
        zFile.close();
        i+=1
        # break
