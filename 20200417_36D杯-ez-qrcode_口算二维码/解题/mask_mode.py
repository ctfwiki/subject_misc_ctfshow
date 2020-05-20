import math

def mask(mask,row,column):
    if mask == 0:
        return (row + column) % 2 == 0
    elif mask == 1:
        return (row) % 2 == 0
    elif mask == 2:
        return (column) % 3 == 0
    elif mask == 3:
        return (row + column) % 3 == 0
    elif mask == 4:
        return (math.floor(row / 2) + math.floor(column / 3)) % 2 == 0
    elif mask == 5:
        return ((row * column) % 2) + ((row * column) % 3) == 0
    elif mask == 6:
        return ( ((row * column) % 2) + ((row * column) % 3) ) % 2 == 0
    elif mask == 7:
        return ( ((row + column) % 2) + ((row * column) % 3) ) % 2 == 0
    else:
        exit("未知的掩码模式")
