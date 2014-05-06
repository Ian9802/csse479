from AES import math

rate = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002,
        .008, .040, .024, .067, .075, .019, .001, .060, .063, .091,
        .028, .010, .023, .001, .020, .001]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']


def main():
    print("Vigenere Cipher")
    #list input for text
    text = input("text\n").lower()
    out = decrypt(text)
    for item in out:
        print(item)


def decrypt(text):
    keyLengths = keySize(text)
    for length in keyLengths:
        print(length)
    size = int(input("size to try\n"))
    possibleKey = getKey(text, size)
    listText = list(text)
    for i in range(0, len(possibleKey)):
        listText = codeBreak(listText, i, size, possibleKey[i])
    textKey = []
    a = ord('a')
    for i in range(0, len(possibleKey)):
        textKey.append(chr(possibleKey[i]+a))
    return [[textKey], [listText]]

def keySize(text):
    dataList = []
    for i in range(1, len(text)):
        dataList.append((collisions(text, i), i))
    returnList = sorted(dataList)
    returnList.reverse()
    return returnList


def collisions(text, offset):
    count = 0
    for i in range(offset, len(text)):
        if text[i] == text[i - offset]:
            count += 1
    return count


def getKey(text, size):
    returnList = []
    for i in range(0, size):
        returnList.append(findLetter(text, i, size))
    return returnList


def findLetter(text, point, size):
    results = []

    a = ord('a')

    for i in range(0, 26):
        freqency = freq(text, point, size, i)
        results.append((dot(freqency, rate), i))
    fixedResults = sorted(results)
    fixedResults.reverse()
    return fixedResults[0][1]


def freq(list, point, size, shift):
    countList = []
    returnFrequencies = []
    count = 0
    a = ord('a')
    for i in range(0, 26):
        countList.append(0)
    for j in range(0, len(list)):
        if point == j % size:
            countList[(ord(list[j]) - a + shift) % 26] += 1
        else:
            countList[ord(list[j]) - a] += 1
        count += 1
    for rate in countList:
        returnFrequencies.append(rate / count)
    return returnFrequencies


def dot(list1, list2):
    returnList = []
    size = 0
    for i in range(0, len(list1)):
        returnList.append(list1[i] * list2[i])
    for item in returnList:
        size += item
    return math.cos(size)


def codeBreak(text, point, size, shift):
    numText = []
    a = ord('a')
    for letter in text:
        numText.append(ord(letter) - a)
    print(numText)
    for i in range(point, len(text), size):
        numText[i] -= shift
        numText[i] %= 26

    stringText = []
    for num in numText:
        stringText.append(chr(num+a))

    return stringText

#    returnMessage = []
#    a = ord('a')
#    for i in range(point, len(text), size):
#        returnMessage.append(chr(((ord(text[i]) - shift) % 26) + a))
#    return returnMessage

if __name__ == '__main__':
    main()






