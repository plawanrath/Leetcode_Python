'''
x = 11
y = 01

while y:

1.    res = 11 ^ 01 = 10
      carry = (11 & 01) << 1 = 1 << 1 = 010 # left shift simply appends 0s to the right of the binary
      x = 010, y = 010
2.     res  = 010 ^ 010 = 000
       carry = (010 & 010) << 1 = 010 << 1 = 0100
        x = 0000, y = 0100
3.     res = 0000 ^ 0100 = 0100
       carry = (0000 & 0100) << 1 = 0000 << 1 = 0000

       answer = 100
'''
def addBinary(a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    # use x to store result and y to store carry
    while y:
        res = x ^ y # answer without carry is XOR
        carry = (x & y) << 1 # carry will be left shifted and
        x, y = res, carry
    return bin(x)[2:]

a = "11"
b = "1"

print(addBinary(a, b))