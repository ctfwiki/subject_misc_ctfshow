import math

import type_info,mask_mode#,data_decode

binstr = "1111111010101011111010111111110000010101101111101001000001101110101000001100111010111011011101001110110110100101110110111010011011100011101011101100000101111010110100010000011111111010101010101010111111100000000111101000001100000000001110101101111010110111001111100000000111011010000111101101110110100001100100100101100010001010101010101001101010111010011010001010100100011010010110001101111000001111111110101001111000000011001001000001111110101011110101000000101010000010001111101100100000100101010000111000001111011110111001111011011010100010001100010111100010110100000101001011101110100001001110001111111000000000010011000010010001000111111110010100110011101011000100000100111010110111000110011011101010111010100011111010110111010110101011011100101000101110101110101100100101100101000001000110111001011010101011111110010011011011001110000"

size = int(math.sqrt(len(binstr)))
print("二维码尺寸：",size)
if size != 29:
    exit("暂不支持该尺寸")

version = int((size - 17) / 4)
print("version：",version)

qrcode = []
for y in range(size):
    qrcode.append([])
    for x in range(size):
        qrcode[y].append(binstr[y*size+x])

tinfo = "".join(qrcode[8][-8:])
print("type_info：",tinfo)

ECCLevel,MaskPattern = type_info.getlevel(tinfo)
print("纠错级别：",ECCLevel)
print("掩码模式",MaskPattern)

def mv(row, column):
    # print(row,column)
    val = qrcode[row][column]
    if mask_mode.mask(MaskPattern,row,column):
        if val == '1':
            val = '0'
        else:
            val = '1'
    return val

def p8(type,y,x):
    if type == 1:
        return mv(y,x)+mv(y,x-1)+mv(y-1,x)+mv(y-1,x-1)+mv(y-2,x)+mv(y-2,x-1)+mv(y-3,x)+mv(y-3,x-1)
    elif type == 2:
        return mv(y,x)+mv(y,x-1)+mv(y+1,x)+mv(y+1,x-1)+mv(y+2,x)+mv(y+2,x-1)+mv(y+3,x)+mv(y+3,x-1)
    elif type == 3:
        return mv(y,x)+mv(y,x-1)+mv(y-1,x)+mv(y-1,x-1)+mv(y-2,x)+mv(y-2,x-1)+mv(y-2,x-2)+mv(y-2,x-3)
    elif type == 4:
        return mv(y,x)+mv(y,x-1)+mv(y+1,x)+mv(y+1,x-1)+mv(y+7,x)+mv(y+7,x-1)+mv(y+8,x)+mv(y+8,x-1)
    elif type == 5:
        return mv(y,x)+mv(y,x-1)+mv(y+1,x)+mv(y+1,x-1)+mv(y+1,x-2)+mv(y+1,x-3)+mv(y,x-2)+mv(y,x-3)
    elif type == 6:
        return mv(y,x)+mv(y,x-1)+mv(y-1,x)+mv(y-1,x-1)+mv(y-2,x-1)+mv(y-3,x-1)+mv(y-4,x-1)+mv(y-5,x-1)
    elif type == 7:
        return mv(y,x)+mv(y-1,x+1)+mv(y-1,x)+mv(y-2,x+1)+mv(y-2,x)+mv(y-3,x+1)+mv(y-3,x)+mv(y-4,x+1)
    elif type == 8:
        return mv(y,x)+mv(y-1,x+1)+mv(y-1,x)+mv(y-3,x+1)+mv(y-3,x)+mv(y-4,x+1)+mv(y-4,x)+mv(y-5,x+1)
    elif type == 9:
        return mv(y,x)+mv(y-1,x+1)+mv(y-1,x)+mv(y-2,x+1)+mv(y-2,x)+mv(y-3,x+1)+mv(y-3,x)+mv(y-3,x-1)
    elif type == 10:
        return mv(y,x)+mv(y+1,x+1)+mv(y+1,x)+mv(y+2,x+1)+mv(y+2,x)+mv(y+3,x+1)+mv(y+3,x)+mv(y+4,x+1)
    elif type == 11:
        return mv(y,x)+mv(y+1,x+1)+mv(y+1,x)+mv(y+3,x+1)+mv(y+3,x)+mv(y+4,x+1)+mv(y+4,x)+mv(y+5,x+1)

D1 = p8(1,size-1,size-1)
D14 = p8(1,size-5,size-1)
D2 = p8(1,size-9,size-1)
D15 = p8(1,size-13,size-1)
D3 = p8(1,size-17,size-1)

D16 = p8(2,size-20,size-3)
D4 = p8(2,size-16,size-3)
D17 = p8(2,size-12,size-3)
D5 = p8(2,size-8,size-3)
D18 = p8(2,size-4,size-3)

D6 = p8(1,size-1,size-5)
D19 = p8(1,size-10,size-5)
D7 = p8(1,size-14,size-5)

D20 = p8(3,size-18,size-5)

D8 = p8(2,size-19,size-7)
D21 = p8(2,size-15,size-7)

D9 = p8(4,size-11,size-7)
D22 = p8(5,size-2,size-7)
D10 = p8(6,size-3,size-9)

D23 = p8(7,size-9,size-10)
D11 = p8(7,size-13,size-10)
D24 = p8(7,size-17,size-10)

D12 = p8(8,size-21,size-10)
D25 = p8(9,size-26,size-10)
D13 = p8(10,size-29,size-12)
D26 = p8(11,size-25,size-12)

binstr2 = D1+D2+D3+D4+D5+D6+D7+D8+D9+D10+D11+D12+D13+D14+D15+D16+D17+D18+D19+D20+D21+D22+D23+D24+D25+D26
print("encoded qrbin：",binstr2)

# binstr2 = "0010000000110100111110100100010100010001001111010000010010011110110101000001010011011101110100100101010001001110010110010000111001010001110110101001001011010101000110010001000100001110000100100001111101000000"
# content = data_decode.decode(binstr2,version)
# print("二维码内容：",content)
