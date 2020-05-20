from base全家桶 import *
import random

def ran(a,b):# [a,b]
    return random.randint(a,b)

def gen_base_txt():
    string = base64_encode_apple(test_string)
    print(string)
    i16 = i32 = i64 = i58 = i85 = i91 = i92 = 0
    # print(i16,i32)
    cengshu = 5
    while i16 < cengshu or i32 < cengshu or i64 < cengshu or i58 < cengshu or i85 < cengshu or i91 < cengshu or i92 < cengshu:
        i = ran(1,7)
        print(i)
        if i == 1:
            if i16 < cengshu:
                string = eb16(string)
                i16 += 1
        elif i == 2:
            if i32 < cengshu:
                string = eb32(string)
                i32 += 1
        elif i == 3:
            if i64 < cengshu:
                string = eb64(string)
                i64 += 1
        elif i == 4:
            if i58 < cengshu:
                string = eb58(string)
                i58 += 1
        elif i == 5:
            if i85 < cengshu:
                string = eb85(string)
                i85 += 1
        elif i == 6:
            if i91 < cengshu:
                string = eb91(string)
                i91 += 1
        elif i == 7:
            if i92 < cengshu:
                string = eb92(string)
                i92 += 1
    print(i16 , i32 , i64 , i58 , i85 , i91 , i92, len(string))
    f=open("BaseAllInOne.txt",'w')
    f.write(string)
    f.close()

gen_base_txt()
