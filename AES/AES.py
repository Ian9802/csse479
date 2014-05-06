sBox = [
    [ 99, 124, 119, 123, 242, 107, 111, 197,  48,   1, 103,  43, 254, 215, 171, 118],
    [202, 130, 201, 125, 250,  89,  71, 240, 173, 212, 162, 175, 156, 164, 114, 192],
    [183, 253, 147,  38,  54,  63, 247, 204,  52, 165, 229, 241, 113, 216,  49,  21],
    [  4, 199,  35, 195,  24, 150,   5, 154,   7,  18, 128, 226, 235,  39, 178, 117],
    [  9, 131,  44,  26,  27, 110,  90, 160,  82,  59, 214, 179,  41, 227,  47, 132],
    [ 83, 209,   0, 237,  32, 252, 177,  91, 106, 203, 190,  57,  74,  76,  88, 207],
    [208, 239, 170, 251,  67,  77,  51, 133,  69, 249,   2, 127,  80,  60, 159, 168],
    [ 81, 163,  64, 143, 146, 157,  56, 245, 188, 182, 218,  33,  16, 255, 243, 210],
    [205,  12,  19, 236,  95, 151,  68,  23, 196, 167, 126,  61, 100,  93,  25, 115],
    [ 96, 129,  79, 220,  34,  42, 144, 136,  70, 238, 184,  20, 222,  94,  11, 219],
    [224,  50,  58,  10,  73,   6,  36,  92, 194, 211, 172,  98, 145, 149, 228, 121],
    [231, 200,  55, 109, 141, 213,  78, 169, 108,  86, 244, 234, 101, 122, 174,   8],
    [186, 120,  37,  46,  28, 166, 180, 198, 232, 221, 116,  31,  75, 189, 139, 138],
    [112,  62, 181, 102,  72,   3, 246,  14,  97,  53,  87, 185, 134, 193,  29, 158],
    [225, 248, 152,  17, 105, 217, 142, 148, 155,  30, 135, 233, 206,  85,  40, 223],
    [140, 161, 137,  13, 191, 230,  66, 104,  65, 153,  45,  15, 176,  84, 187,  22]
]


cdKey = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]


def main():
    key, data = readDoc()
    count = int(input("Input the run count:"))
    for i in range(0, count):
        tempdata = execution(key[0], data)
        data = outData(tempdata)
    writeDoc(data)


def outData(data):
    # converts from array of 'matrices' or integers to an array of binary strings
    outValue = list()
    for message in data:
        outString = ""
        for row in message:
            for value in row:
                outString += '{0:08b}'.format(value)
        outValue.append(outString)
    return outValue


def execution(key, data):
    outData = list()
    for row in data:
        #converts from binary to matrix
        base = convert(start(row))
        keyBox = convert(keystart(key))
        tKey = transpose(keyBox)
        #begin AES
        #stage 0
        aBox = ark(base, tKey)
        for x in range(0, 9):
            bBox = bs(aBox)
            cBox = sr(bBox)
            dBox = mc(cBox)
            keyBox = nkb(keyBox, x)
            tKey = transpose(keyBox)
            aBox = ark(dBox, tKey)
        #stage 10
        bBox = bs(aBox)
        cBox = sr(bBox)
        keyBox = nkb(keyBox, 9)
        tKey = transpose(keyBox)
        aBox = ark(cBox, tKey)
        #end AES
        outData.append(transpose(aBox))
    return outData


def convert(inValue):
    #builds array of ints from array of strings of binary
    outValue = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            outValue[x].append(int(inValue[x][y], 2))
    return outValue


def start(binString):
    #builds column indexed array of binary strings
    aBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            aBox[y % 4].append(binString[(32*x)+(8*y):(32*x)+(8*y)+8])
    return aBox


def keystart(binString):
    #build row indexed array of binary strings
    #this is here because all of the key functions were already written in row index
    #transpose flips things back and forth so they match with the functions and
    #I don't have to re-re-re-re-rewrite the key functions.
    keyBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            keyBox[x].append(binString[(32*x)+(8*y):(32*x)+(8*y)+8])
    return keyBox


def bs(aBox):
    #byte substitution, uses the sBox matrix at the top
    #matrix here
    bBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            #value here
            bBox[x].append(indBS(aBox[x][y]))
    return bBox


def indBS(b):
    #finds the value for int input in the sBox
    val = '{0:08b}'.format(b)
    row = val[:4]
    col = val[4:]
    decRow = int(row, 2)
    decCol = int(col, 2)
    return sBox[decRow][decCol]


def sr(bBox):
    #shift row on the input matrix
    #matrix here
    cBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            #value here
            cBox[x].append(bBox[x][(y+x) % 4])
    return cBox


def mc(cBox):
    #mix column transformation
    #matrix here
    dBox = [[] for foo in range(0, 4)]
    tcBox = transpose(cBox)
    for x in range(0, 4):
        #column here
        dBox[x].extend(mux(tcBox[x]))
    return transpose(dBox)


def mux(col):
    #does the individual mix column transformation for the columns themselves
    column = list()
    for x in range(0, 4):
        value = 0
        for y in range(0, 4):
            #this was a pain to get right
            value = value ^ (finiteMult(cdKey[x][y], col[y]))
        column.append(value)
    return column

def finiteMult(a, b):
    #does multiplication in a finite field, built from the guide at:
    #http://en.wikipedia.org/wiki/Finite_field_arithmetic
    #(with a little bit of cleverness and magic)
    aString = '{0:08b}'.format(a)
    bString = '{0:08b}'.format(b)
    p = 0
    for x in range(0, 8):
        if(bString[-1] == '1'):
            p = p ^ a
        b = b >> 1
        carry = (aString[0] == '1')
        a = (a << 1) % 256
        if(carry):
            a = a ^ 27
        aString = '{0:08b}'.format(a)
        bString = '{0:08b}'.format(b)
    return p

def transpose(matrix):
    #transposes a matrix
    box = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            box[y % 4].append(matrix[x][y])
    return box

def ark(dBox, keyBox):
    #Add Round Key, does the round key addition for matrices dBox and keyBox
    #matrix here
    eBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        for y in range(0, 4):
            #value here
            val = dBox[x][y] ^ keyBox[x][y]
            eBox[x].append(val)
    return eBox


def nkb(oldKeyBox, i):
    #New Key Box, follows the key schedule rules to produce the next key box.
    #matrix here
    keyBox = [[] for foo in range(0, 4)]
    for x in range(0, 4):
        #column here
        if x % 4 == 0:
            #4|i
            keyBox[x].extend(wFun(oldKeyBox[x], tFun(oldKeyBox[3], (i+1)*4)))
        else:
            #4∤i
            keyBox[x].extend(wFun(oldKeyBox[x], keyBox[(x-1)]))
    return keyBox


def wFun(col1, col2):
    #W function, xors the input columns
    #column here
    column = list()
    for x in range(0, 4):
        #value here
        column.append(col1[x] ^ col2[x])
    return column


def tFun(oldColumn, i):
    #T function, generates the T column
    #column here
    tempColumn = list()
    returnColumn = list()
    for x in range(0, 4):
        #rotates column up and stores in temp
        tempColumn.append(indBS(oldColumn[(x+1) % 4]))
    #round constant
    c = roundC(i)
    #produces e xor r(i)
    returnColumn.append(c ^ tempColumn[0])
    for x in range(1, 4):
        #stores rest of column
        returnColumn.append(tempColumn[x])
    #not the most space nor time efficient function, but it works and is sturdy.
    return returnColumn


def roundC(val):
    #comuptes the round constant off of the value input
    out = 1
    for x in range(0, (val-4)//4):
        #more finite field multiplication!
        out = finiteMult(out, 2)
    return out


def readDoc():
    #reads in the document
    file = open("aesinput.txt", 'r')
    data = list()
    for line in file:
        data.append(line.rstrip('\n'))
    file.close()
    return data[:1], data[1:]


def writeDoc(data):
    #writes out the document
    file = open("aesianhallamout.txt", 'w')
    for message in data:
        file.write(message)
        file.write('\n')
    file.close()


if __name__ == '__main__':
    main()