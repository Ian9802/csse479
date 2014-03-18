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

#rates of letters in English
rate = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002,
        .008, .040, .024, .067, .075, .019, .001, .060, .063, .091,
        .028, .010, .023, .001, .020, .001]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
#counts of each letter by cypher length
counts = []
#split text by cypher length 1,6,11,etc
textSplit = list()
#size for each split
size = []
#frequency of each letter
frequency = []
#dot product of frequencies with rate
dotRate = []
#sorted likelihoods of dot changes
sd = []


#sets up arrays
for i in range(0, keyLength):
    textSplit.append(list())
    size.append(0)
    frequency.append(list())
    dotRate.append(list())
    counts.append(list())
    for j in range(0, 26):
        counts[i].append(0)

#splits the array
for i in range(0, len(textArray)):
    textSplit[i % keyLength].append(textArray[i])

#gets letter count
a = ord('a')
for i in range(0, len(textSplit)):
    for letters in textSplit[i]:
        counts[i][ord(letters) - a] += 1
        size[i] += 1

#gets frequency
for i in range(0, len(counts)):
    for letter in counts[i]:
        frequency[i].append(letter/size[i])

for i in range(0, len(frequency)):
    for j in range(0, len(frequency[i])):
        dotRate[i].append((dot(shift(frequency[i], j), rate), j))

for item in dotRate:
    inValue = sorted(item)
    inValue.reverse()
    sd.append(inValue)

for item in sd:
    print(chr(item[0][1]+a))

#dotCheck.append(dot(shift(frequency, i), rate))