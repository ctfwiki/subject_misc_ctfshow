import zipfile,os

miniZip_path = "./lib/minizip.exe"

def yasuo(password):
    cmd = '{} -o -1 -p "{}" "{}" "{}"'.format(miniZip_path,password,"./lib/123.zip","lib/123.jpg")
    os.system(cmd)
    print(cmd)

def jieya(password):
    zFile = zipfile.ZipFile("./lib/123.zip", "r")
    for fileM in zFile.namelist():
        zFile.extract(fileM, "./lib/", pwd=password.encode("gbk"))
    zFile.close();

# 冰川时代.jpg
password="冰川时代"
yasuo(password)
jieya(password)
