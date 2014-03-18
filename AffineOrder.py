import fractions
print("Affine Cipher")
text = input()
text = text.lower()
textArray = list(text)
numArray = []
printArray = []
multiplier = []
for i in range(0, 26):
    if fractions.gcd(i, 26) == 1:
        multiplier.append(i)
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

rate = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002,
        .008, .040, .024, .067, .075, .019, .001, .060, .063, .091,
        .028, .010, .023, .001, .020, .001]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

options = []
totalCount = 0
a = ord('a')
for letter in textArray:
    numArray.append(ord(letter) - a)
for i in range(0, 26):
    for j in multiplier:
        for number in numArray:
            printArray.append(chr((j * (number - i)) % 26 + a))
        options.append(''.join(printArray))
        printArray[:] = []

counts = []
for i in range(0, len(options)):
    counts.append([])
    for j in range(0, 26):
        counts[i].append(0)

totalCount = len(textArray)
for i in range(0, len(options)):
    for letter in options[i]:
        value = ord(letter)-a
        counts[i][value] += 1

frequency = []
for i in range(0, len(options)):
    frequency.append([])
for i in range(0, len(options)):
    for letterCount in counts[i]:
        frequency[i].append(letterCount/totalCount)

likelihood = []
for i in range(0, len(options)):
    likelihood.append((dot(frequency[i], rate), options[i]))

output = sorted(likelihood)
output.reverse()
for out in output:
    print(out[1])