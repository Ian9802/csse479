def main():
    text = input("text\n")
    text = text.lower()
    textArray = list(text)
    key = input("key\n")
    key = key.lower()
    keyArray = keyFix(list(key))
    keyMatrix = buildMatrix(keyArray)
    outValue = decipher(textArray, keyMatrix)
    print(''.join(outValue))


def keyFix(keyList):
    returnList = []
    for letter in keyList:
        if letter == 'j':
            letter == 'i'
        if letter not in returnList:
            returnList.append(letter)
    return returnList


def buildMatrix(keyArray):
    a = ord('a')
    for i in range(0, 26):
        letter = chr(i+a)
        if letter == 'j':
            letter = 'i'
        if letter not in keyArray:
            keyArray.append(letter)
    returnMatrix = []
    for i in range(0, 5):
        returnMatrix.append([])
    for i in range(0, 5):
        for j in range(0, 5):
            returnMatrix[i].append(keyArray[i*5+j])
    return returnMatrix


def decipher(textArray, keyArray):
    returnList = []
    for pair in range(0, len(textArray)//2):
        shift = pair*2
        returnList.extend(decipherPair(textArray[shift], textArray[shift+1], keyArray))
    return returnList


def decipherPair(letter1, letter2, keyArray):
    if letter1 == 'j':
        letter1 == 'i'
    if letter2 == 'j':
        letter1 == 'i'
    row1 = 0
    column1 = 0
    row2 = 0
    column2 = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if(keyArray[i][j] == letter1):
                row1 = i
                column1 = j
            if(keyArray[i][j] == letter2):
                row2 = i
                column2 = j
    if row1 == row2:
        column1 -= 1
        column1 %= 5
        column2 -= 1
        column2 %= 5
        return [keyArray[row1][column1], keyArray[row2][column2]]
    if column1 == column2:
        row1 -= 1
        row1 %= 5
        row2 -= 1
        row2 %= 1
        return [keyArray[row1][column1], keyArray[row2][column2]]
    return [keyArray[row1][column2], keyArray[row2][column1]]


if __name__ == '__main__':
    main()



















