import gmpy2
import libnum
import sympy
import owiener
from Crypto.Util.number import getPrime,getRandomNBitInteger

def write_enc(file,e,n,c):
    if file:
        with open(file,'w') as f:
            f.write("e = %s\n"%e)
            f.write("n = %s\n"%n)
            f.write("c = %s\n"%c)
            f.close()
    else:
        print("e =", e)
        print("n =", n)
        print("c =", c)

# babyrsa
def babyrsa(flag,file=None):
    e = 0x10001
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q

    m = libnum.s2n(flag)
    c = pow(m,e,n)
    if file:
        with open(file,'w') as f:
            f.write("e = %s\n"%e)
            f.write("p = %s\n"%p)
            f.write("q = %s\n"%q)
            f.write("c = %s\n"%c)
            f.close()
    else:
        print("e =", e)
        print("p =", p)
        print("q =", q)
        print("c =", c)


# easyrsa1
def easyrsa1(flag,file=None):
    e = 0x10001
    p = getPrime(100)
    q = getPrime(100)
    n = p * q
    m = libnum.s2n(flag)
    c = pow(m,e,n)
    write_enc(file,e,n,c)

# easyrsa2
def easyrsa2(flag,file=None):
    e = 0x10001
    p = getPrime(1024)
    q1 = getPrime(1024)
    q2 = getPrime(1024)
    n1 = p*q1
    n2 = p*q2
    m = libnum.s2n(flag)
    c1 = pow(m,e,n1)
    c2 = pow(m,e,n2)
    if file:
        with open(file,'w') as f:
            f.write("e = %s\n"%e)
            f.write("n = %s\n"%n1)
            f.write("c = %s\n\n"%c1)
            f.write("e = %s\n"%e)
            f.write("n = %s\n"%n2)
            f.write("c = %s\n"%c2)
            f.close()
    else:
        print("e =", e)
        print("n =", n1)
        print("c =", c1)
        print()
        print("e =", e)
        print("n =", n2)
        print("c =", c2)

# easyrsa3
def easyrsa3(flag,file=None):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    m = libnum.s2n(flag)
    e1 = getPrime(10)
    c1 = pow(m, e1, n)
    e2 = getPrime(10)
    c2 = pow(m, e2, n)
    if file:
        with open(file,'w') as f:
            f.write("e = %s\n"%e1)
            f.write("n = %s\n"%n)
            f.write("c = %s\n\n"%c1)
            f.write("e = %s\n"%e2)
            f.write("n = %s\n"%n)
            f.write("c = %s\n"%c2)
            f.close()
    else:
        print("e =", e1)
        print("n =", n)
        print("c =", c1)
        print()
        print("e =", e2)
        print("n =", n)
        print("c =", c2)

def easyrsa4(flag,file=None):
    e = 3
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    m = libnum.s2n(flag)
    c = pow(m,e,n)
    write_enc(file,e,n,c)

def easyrsa5(flag,file=None):
    # from rsa_wiener_attack.RSAvulnerableKeyGenerator import generateKeys
    e = 284100478693161642327695712452505468891794410301906465434604643365855064101922252698327584524956955373553355814138784402605517536436009073372339264422522610010012877243630454889127160056358637599704871937659443985644871453345576728414422489075791739731547285138648307770775155312545928721094602949588237119345
    n = 468459887279781789188886188573017406548524570309663876064881031936564733341508945283407498306248145591559137207097347130203582813352382018491852922849186827279111555223982032271701972642438224730082216672110316142528108239708171781850491578433309964093293907697072741538649347894863899103340030347858867705231
    m = libnum.s2n(flag)
    c = pow(m,e,n)
    write_enc(file,e,n,c)

def easyrsa7(flag,file=None):
    e = 0x10001
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    m = libnum.s2n(flag)
    c = pow(m,e,n)
    if file:
        with open(file,'w') as f:
            f.write("e = %s\n"%hex(e))
            f.write("p>>128<<128 =%s\n"%hex(p>>128<<128))
            f.write("n = %s\n"%hex(n))
            f.write("c = %s\n"%hex(c))
            f.close()
    else:
        print("e =", hex(e))
        print("p>>128<<128 =", hex(p>>128<<128))
        print("n =", hex(n))
        print("c =", hex(c))

def funnyrsa1(flag,file=None):
    p = getPrime(1024)
    m = libnum.s2n(flag)
    # print("m =",m)
    gcd = 14

    e1 = getPrime(50) * gcd
    q1 = getPrime(1024)
    while True:
        phi = (p - 1) * (q1 - 1)
        if phi % gcd == 0:
            break
        else:
            q1 = getPrime(1024)
    c1 = pow(m, e1, p * q1)

    e2 = getPrime(50) * gcd
    q2 = getPrime(1024)
    while True:
        phi = (p - 1) * (q2 - 1)
        if phi % gcd == 0 and gmpy2.gcd(e1,(q1-1)*(q2-1))==2:
            break
        else:
            q2 = getPrime(1024)
    c2 = pow(m, e2, p * q2)
    # c1 = pow(m, e1, p * q1)
    # c2 = pow(m, e2, p * q2)
    if file:
        with open(file,'w') as f:
            f.write("e1 = %s\n"%e1)
            f.write("p1 =%s\n"%p)
            f.write("q1 = %s\n"%q1)
            f.write("c1 = %s\n\n"%c1)
            f.write("e2 = %s\n"%e2)
            f.write("p2 =%s\n"%p)
            f.write("q2 = %s\n"%q2)
            f.write("c2 = %s\n\n"%c2)
            f.close()
    else:
        print("p =", p)
        print("e1 =", e1)
        print("q1 =", q1)
        print("c1 =", c1)

        print("e2 =", e2)
        print("q2 =", q2)
        print("c2 =", c2)

def funnyrsa3(flag,file=None):
    e = 0x10001
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    d = d_epq(e,p,q)
    dp = d%(p-1)
    m = libnum.s2n(flag)
    c = pow(m,e,n)
    if file:
        with open(file,'w') as f:
            f.write("e = %s\n"%e)
            f.write("n =%s\n"%n)
            f.write("dp = %s\n"%dp)
            f.write("c = %s\n"%c)
            f.close()
    else:
        print("e =", e)
        print("n =", n)
        print("dp =", dp)
        print("c =", c)

if __name__ == '__main__':
    # print("babyrsa"+"="*50)
    # babyrsa("flag{b4by_R5A}")
    #
    # print("easyrsa1"+"="*50)
    # easyrsa1("flag{fact0r_sma11_N}")
    #
    # print("easyrsa2"+"="*50)
    # easyrsa2("flag{m0_bv_hv_sv}")

    # print("easyrsa3"+"="*50)
    # easyrsa3("flag{sh4r3_N}","easyrsa3.txt")

    # print("easyrsa4"+"="*50)
    # easyrsa4("flag{Sm4ll_eee}")
    #
    # print("easyrsa5"+"="*50)
    # easyrsa5("flag{very_biiiiig_e}","easyrsa5.txt")
    #
    # print("easyrsa7"+"="*50)
    # easyrsa7("flag{Kn0wn_Hi9h_Bit5}")
    #
    print("funnyrsa1"+"="*50)
    funnyrsa1("flag{gcd_e&φ_isn't_1}","funnyrsa1.txt")
    #
    # print("funnyrsa3"+"="*50)
    # funnyrsa3("flag{dp_i5_1eak}")
