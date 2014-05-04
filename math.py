
def finiteMult(a, b):
    aString = '{0:08b}'.format(a)
    bString = '{0:08b}'.format(b)
    p = 0
    for x in range(0, 8):
        if(bString[-1] == '1'):
            p = p ^ a
        b = b >> 1
        carry = (aString[0] == '1')
        a = (a << 1)%256
        if(carry):
            a = a ^ 27
        aString = '{0:08b}'.format(a)
        bString = '{0:08b}'.format(b)
    return p

print(finiteMult(87,131))