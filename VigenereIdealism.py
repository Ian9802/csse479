from pip.backwardcompat import raw_input

print("Vigenere Cipher")
#text input for text
text = input()
text = text.lower()
textArray = list(text)
#int input for key length
keyLength = int(raw_input())


#dot product
def dot(list1, list2):
    RL = []
    size = 0
    for i in range(0, len(list1)):
        RL.append(list1[i] * list2[i])
    for item in RL:
        size += item
    return size


#returns a shifted list, shifted by the shift value
def shift(list, shift):
    RL = []
    for i in range(shift, len(list)):
        RL.append(list[i])
    for i in range(0,shift):
        RL.append(list[i])
    return RL
def freq(list):
    countList = []
    RF = []
    count = 0
    a = ord('a')
    for i in range(0, 26):
        countList.append(0)
    for letter in list:
        countList[ord(letter)-a] += 1
        count += 1
    for rate in countList:
        RF.append(rate/count)
    return RF

#rates of letters in English
rate = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002,
        .008, .040, .024, .067, .075, .019, .001, .060, .063, .091,
        .028, .010, .023, .001, .020, .001]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

cypher = []
frequency = []
testList = []
for i in range(0, 26):
    testList.append(list())

a = ord('a')
for i in range(0, keyLength):
    for j in range(0, len(textArray)):
        for k in range(0, 26):
            if j % keyLength == i:
                testList[k].append(chr(((ord(textArray[j])+k) % 26) + a))
            else:
                testList[k].append(textArray[j])
    for l in range(0, 26):
        frequency.append((dot(freq(testList[l]), rate), l))
    temp = sorted(frequency)
    temp.reverse()
    if i == 1:
        for item in temp:
            print(item)
    cypher.append(temp[0][1])
    frequency[:] = []
    temp[:] = []
    testList[:] = []
    for m in range(0, 26):
        testList.append(list())

for letter in cypher:
    print(chr(letter+a))