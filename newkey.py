sBox = [
    [ 99,124,119,123,242,107,111,197, 48,  1,103, 43,254,215,171,118],
    [202,130,201,125,250, 89, 71,240,173,212,162,175,156,164,114,192],
    [183,253,147, 38, 54, 63,247,204, 52,165,229,241,113,216, 49, 21],
    [  4,199, 35,195, 24,150,  5,154,  7, 18,128,226,235, 39,178,117],
    [  9,131, 44, 26, 27,110, 90,160, 82, 59,214,179, 41,227, 47,132],
    [ 83,209,  0,237, 32,252,177, 91,106,203,190, 57, 74, 76, 88,207],
    [208,239,170,251, 67, 77, 51,133, 69,249,  2,127, 80, 60,159,168],
    [ 81,163, 64,143,146,157, 56,245,188,182,218, 33, 16,255,243,210],
    [205, 12, 19,236, 95,151, 68, 23,196,167,126, 61,100, 93, 25,115],
    [ 96,129, 79,220, 34, 42,144,136, 70,238,184, 20,222, 94, 11,219],
    [224, 50, 58, 10, 73,  6, 36, 92,194,211,172, 98,145,149,228,121],
    [231,200, 55,109,141,213, 78,169,108, 86,244,234,101,122,174,  8],
    [186,120, 37, 46, 28,166,180,198,232,221,116, 31, 75,189,139,138],
    [112, 62,181,102, 72,  3,246, 14, 97, 53, 87,185,134,193, 29,158],
    [225,248,152, 17,105,217,142,148,155, 30,135,233,206, 85, 40,223],
    [140,161,137, 13,191,230, 66,104, 65,153, 45, 15,176, 84,187, 22]
]

key =[['00000000', '00000001', '00000010', '00000011'],
['00000100', '00000101', '00000110', '00000111'],
['00001000', '00001001', '00001010', '00001011'],
['00001100', '00001101', '00001110', '00001111']]

def indBS(b):
    val = '{0:08b}'.format(b)
    row = val[:4]
    col = val[4:]
    decRow = int(row, 2)
    decCol = int(col, 2)
    return sBox[decRow][decCol]


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
            a = a ^ 27
        aString = '{0:08b}'.format(a)
        bString = '{0:08b}'.format(b)
    return p

def nkb(oldKeyBox, i):
    print(oldKeyBox)
    print(i)
    keyBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        if x % 4 == 0:
            keyBox[x].extend(wFun(oldKeyBox[x], tFun(oldKeyBox[3], (i+1)*4)))
        else:
            keyBox[x].extend(wFun(oldKeyBox[x], keyBox[(x-1)]))
    print(keyBox)
    return keyBox


def wFun(col1, col2):
    column = list()
    for x in range(0, 4):
        column.append(col1[x] ^ col2[x])
    return column


def tFun(oldColumn, i):
    tempColumn = list()
    returnColumn = list()
    for x in range(0, 4):
        tempColumn.append(indBS(oldColumn[(x+1) % 4]))
    c = roundC(i)
    returnColumn.append(c ^ tempColumn[0])
    for x in range(1, 4):
        returnColumn.append(tempColumn[x])
    return returnColumn

def roundC(val):
    out = 1
    for x in range(0, (val-4)//4):
        out = finiteMult(out, 2)
    return out


def hexBox(matrix):
    box = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            box[x].append(hex(matrix[x][y]))
    return box

val = convert(key)
for i in range(0, 10):
    val = nkb(val, i)
    print(hexBox(val))

def transpose(matrix):
    box = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            box[y % 4].append(matrix[x][y])
    return box


