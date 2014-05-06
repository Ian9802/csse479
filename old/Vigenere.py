print("Vigenere Cipher")
#dot
def dot(list1, list2):
    RL = []
    size = 0
    for i in range(0,len(list1)):
        RL.append(list1[i] * list2[i])
    for item in RL:
        size += item
    return size
def shift(list, shift):
    RL = []
    for i in range(shift, len(list)):
        RL.append(list[i])
    for i in range(0,shift):
        RL.append(list[i])
    return RL
def collisions(list, offset):
    count = 0
    for i in range(offset, len(list)):
        if list[i] == list[i-offset]:
            count += 1
    return count

rate = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002,
        .008, .040, .024, .067, .075, .019, .001, .060, .063, .091,
        .028, .010, .023, .001, .020, .001]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 0]
frequency = []
dotCheck = []
totalCount = 0
a = ord('a')
text = input()
text = text.lower()
textArray = list(text)
coincidences = list()
coincidences.append(0)
for i in range(1, len(textArray)):
    coincidences.append(collisions(textArray,i))
for letter in textArray:
    loc = ord(letter)-a
    if 25 >= loc >= 0:
        counts[loc] += 1
        totalCount += 1
for letterCount in counts:
    frequency.append(letterCount/totalCount)
for i in range(0, len(rate)):
    dotCheck.append(dot(shift(frequency, i), rate))
print(coincidences)
print(dotCheck)