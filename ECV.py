print("encrypt Vigenere")
a = ord('a')
text = input()
text = text.lower()
textArray = list(text)
cypher = input()
cypher = text.lower()
cypherArray = list(text)
outArray = []
for i in range(0, len(text)):
    letter = chr(((ord(textArray[i])-a+ord(cypher[i])-a)%26)+a)
    outArray.append(letter)
print(''.join(outArray))