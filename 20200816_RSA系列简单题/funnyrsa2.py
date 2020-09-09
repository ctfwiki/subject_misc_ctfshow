from Crypto.Util.number import getPrime
import libnum
from secret import flag

e = 0x10001
p = getPrime(80)
q = getPrime(80)
r = getPrime(80)
n = p * q * r
m = libnum.s2n(flag)
c = pow(m,e,n)
print("n =", n)
print("c =", c)
# n = 897607935780955837078784515115186203180822213482989041398073067996023639
# c = 490571531583321382715358426750276448536961994273309958885670149895389968
