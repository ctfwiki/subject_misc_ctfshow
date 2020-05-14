from base全家桶 import *
import re

def base64_encode_apple(flag):
    w=""
    k=40
    for j in flag.encode():
    	res=j^k
    	w+=chr(res)
    	k+=1
    return base64.b64encode(w.encode()).decode()

def base64_decode_apple(s):
    s=base64.b64decode(s)
    flag=""
    k=40
    for j in s:
    	res=j^k
    	flag+=chr(res)
    	k+=1
    return flag

base16_table = r'^[A-F0-9=]*$'
base32_table = r'^[A-Z2-7=]*$'
base58_table = r'^[1-9A-HJ-NP-Za-km-z]*$'
base64_table = r'^[A-Za-z0-9/+=]*$'
base85_table = r'^[0-9A-Za-z!#\$%&\(\)\*\+-;<=>\?@\^_`\{\|\}~]*$'
base91_table = r'^[0-9A-Za-z!#\$%&\(\)\*\+,\./:;<=>\?@\[\]\^_`\{\|\}~"]*$'
base92_table = r'^[A-Za-z0-9!#\$%&\(\)\*\+,\./:;<=>\?@\[\]\^_`\{\|\}~" ]*$'

def base_decode(text,step=0):
    if len(text) < 50:
        print(text)
    try:
        step += 1
        if re.match(base16_table,text):
            print("%s--> base16"%step)
            text = base_decode(db16(text),step)
        elif re.match(base32_table,text):
            print("%s--> base32"%step)
            text = base_decode(db32(text),step)
        elif re.match(base58_table,text):
            print("%s--> base58"%step)
            text = base_decode(db58(text),step)
        elif re.match(base64_table,text):
            print("%s--> base64"%step)
            text = base_decode(db64(text),step)
        elif re.match(base85_table,text):
            print("%s--> base85"%step)
            text = base_decode(db85(text),step)
        elif re.match(base91_table,text):
            print("%s--> base91"%step)
            text = base_decode(db91(text),step)
        else:
            print("%s--> base92"%step)
            text = base_decode(db92(text),step)
    finally:
        return text

def dec_base_text():
    f=open("BaseAllInOne.txt")
    string = f.read()
    f2 = open("base.txt",'w')
    f2.write(base_decode(string))
    f2.close()

# dec_base_text()


print(base64_decode_apple("TkVLTFdUQVpvUlNda1ZXRUpAZVldTltgJCQhLCAgGSknPjc="))
