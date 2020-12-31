import sys
from os import system
from calendar import monthrange

year = 1896
month = 1
day = 1

key = ""
endKey = '20200101'

def inttostr(a, n):
    ret = str(a)
    while len(ret) < n:
        ret = '0' + ret
    return ret

def getNextKey():
    global key, endKey
    global year
    global month, day
    if key == endKey:
        return 0
    day = day + 1
    if day > monthrange(year, month)[1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    key = str(year) + inttostr(month, 2) + inttostr(day, 2)
    return 1

img = "guess.jpg"

def main():
    global img
    while getNextKey():
        cmd = "./outguess/outguess -k " + key + " -r " + img + " -t ./output/" + key +".txt"
        system(cmd)
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        img = sys.argv[1]
        print "img: ",img
        if len(sys.argv) > 2 and len(sys.argv[2]) == 8:
            year = int(sys.argv[2][:4])
            month = int(sys.argv[2][4:6])
            day = int(sys.argv[2][6:])
            print "start date: ", year, month, day
            if len(sys.argv) > 3:
                endKey = sys.argv[3]
                print "end date: ", endKey
    main()
