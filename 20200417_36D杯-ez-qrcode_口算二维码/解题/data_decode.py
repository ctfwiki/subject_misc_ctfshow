import re
from enum import Enum

class Mode(Enum):
    NUM_MODE = "0001"
    ALPH_MODE = "0010"
    BYTE_MODE = "0100"
    KANJI_MODE = "1000"
    ECI_MODE = "0111"

#
# loop do
#   case mode = read(data, 4)
#   when '0010' # Alphanumeric
#     count = read(data, 9).to_i(2)
#     (count / 2).times do
#       chunk = read(data, 11).to_i(2)
#       print alphanumeric[chunk / 45] + alphanumeric[chunk % 45]
#     end
#     print alphanumeric[read(data, 11).to_i(2)] if count.odd?
#   when '0100' # Byte
#     count = read(data, 8).to_i(2)
#     count.times do
#       print read(data, 8).to_i(2).chr
#     end
#   when '1000' # Kanji

def numeric_mode(bin):
    return " TODO "

def alpha_mode(bin):
    return " TODO "

def byte_mode(bin):
    b = re.findall(r'.{8}',bin)
    string = ''
    for i in b:
        string += chr(int(i,2))
    return string

def kanji_mode(bin):
    string = ''
    for bin13 in re.findall(r'.{13}',bin):
        num = int(bin13,2)
        if num >= 0x1740:
            string += (0xC140 + num / 0xC0 * 0x100 + num % 0xC0).chr(Encoding::Shift_JIS).encode(Encoding::UTF_8)
        else:
            string += (0x8140 + num / 0xC0 * 0x100 + num % 0xC0).chr(Encoding::Shift_JIS).encode(Encoding::UTF_8)
    return string

def eci_mode(bin):
    return " TODO "


idx = 0

def read(data,length):
    global idx
    res = data[idx:idx+length]
    idx += length
    return res

def getlenlen(version,mode):
    if version < 10:
        if mode == Mode.NUM_MODE.value:
            return 10
        elif mode == Mode.ALPH_MODE.value:
            return 9
        elif mode == Mode.BYTE_MODE.value:
            return 8
        elif mode == Mode.KANJI_MODE.value:
            return 8
    elif version < 27:
        if mode == Mode.NUM_MODE.value:
            return 12
        elif mode == Mode.ALPH_MODE.value:
            return 11
        elif mode == Mode.BYTE_MODE.value:
            return 16
        elif mode == Mode.KANJI_MODE.value:
            return 10
    elif version < 41:
        if mode == Mode.NUM_MODE.value:
            return 14
        elif mode == Mode.ALPH_MODE.value:
            return 13
        elif mode == Mode.BYTE_MODE.value:
            return 16
        elif mode == Mode.KANJI_MODE.value:
            return 12
    return 0

def decode(binstr,version):
    global idx
    content = ""
    while idx < len(binstr):
        mode = read(binstr,4)
        ll = getlenlen(version,mode)
        if ll == 0:
            exit("未知version && mode")
        data_length = int(read(binstr,ll),2)
        if mode == Mode.NUM_MODE.value:
            # Numeric Mode (10 bits per 3 digits)
            data = read(binstr, int(data_length/3) * 10)
            content += numeric_mode(data)
        elif mode == Mode.ALPH_MODE.value:
            # Alphanumeric Mode (11 bits per 2 characters)
            data = read(binstr, int(data_length/2) * 11)
            content += alpha_mode(data)
        elif mode == Mode.BYTE_MODE.value:
            # Byte Mode (8 bits per character)
            data = read(binstr, data_length * 8)
            content += byte_mode(data)
        elif mode == Mode.KANJI_MODE.value:
            # Kanji Mode (13 bits per character)
            data = read(binstr, data_length * 13)
            content += kanji_mode(data)
        elif mode == Mode.ECI_MODE.value:
            # ECI Mode
            pass
        else:
            pass
        print("content:",content)
    return content
