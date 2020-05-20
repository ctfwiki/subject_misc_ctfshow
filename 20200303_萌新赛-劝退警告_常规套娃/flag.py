import base64

arr = ['NQ', 'MQ', 'Mw', 'MA', 'NA', 'Ng', 'Mg', 'OQ', 'Nw', 'OA', 'LQ', 'PQ']

flag = "136-139-78-132-162-89-49-117-70-161-49-118-70-02-01-01-70-137-01-160"

def encode(s):
    return base64.b64encode(s.encode()).decode()

def decode(s):
    return base64.b64decode(s.encode()).decode()

def check(x):
    v = ''
    for c in flag.split(decode(arr[10]+decode(arr[11]+chr(61)*2)*2)):
        n = ''
        for i in c:
            n += decode(arr[int(i)]+decode(arr[11]+chr(61)*2)*2)
        v += chr(int(n))
    if x == 1:
        print v

check(0)

# python3编译
# python -m compileall -b .

# python2编译
# python compileall -l flag.py
