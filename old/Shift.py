print("Shift Cipher")
text = input()
text = text.lower()
textArray = list(text)
numArray = []
printArray = []
a = ord('a')
for letter in textArray:
    numArray.append(ord(letter) - a)
for i in range(0, 26):
    for number in numArray:
        printArray.append(chr((number+i)%26 + a))
    print(''.join(printArray))
    printArray[:] = []