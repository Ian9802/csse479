key =[['00000000', '00000001', '00000010', '00000011'],
['00000100', '00000101', '00000110', '00000111'],
['00001000', '00001001', '00001010', '00001011'],
['00001100', '00001101', '00001110', '00001111']]

ri = ['10001101', '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000', '00011011']

def convert(inValue):
    outValue = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            outValue[x].append(int(inValue[x][y], 2))
    return outValue


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
            print(a)
            a = a ^ 27
            print(a)
        aString = '{0:08b}'.format(a)
        bString = '{0:08b}'.format(b)
    return p

def nkb(oldKeyBox, i):
    keyBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        if x % 4 == 0:
            keyBox[x].extend(wFun(oldKeyBox[x], tFun(oldKeyBox[3], i*4)))
        else:
            keyBox[x].extend(wFun(oldKeyBox[x], keyBox[(x-1)]))
    return keyBox


def wFun(col1, col2):
    column = list()
    for x in range(0, 4):
        column.append(col1[x] ^ col2[x])
    return column


def tFun(oldColumn, i):
    column = list()
    column.append(oldColumn[0] ^ roundC(i))
    for x in range(1, 4):
        column.append(oldColumn[(x+1) % 4])
    return column


def roundC(val):
    out = 1
    for x in range(0, (val-4)//4):
        out = finiteMult(out, 2)
    return out

val = convert(key)
for i in range(0, 10):
    val = nkb(val, i)
    print(val)
