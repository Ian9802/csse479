import fractions
print("Affine Cipher")
text = input()
text = text.lower()
textArray = list(text)
numArray = []
printArray = []
multiplier = []
for i in range(0,26):
    if fractions.gcd(i, 26) == 1:
        multiplier.append(i)
#multiplier = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
a = ord('a')
for letter in textArray:
    numArray.append(ord(letter) - a)
for i in range(0, 26):
    for j in multiplier:
        for number in numArray:
            printArray.append(chr((j * (number - i)) % 26 + a))
        print(''.join(printArray))
        printArray[:] = []