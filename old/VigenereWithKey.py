def main():
    print("Vigenere Cipher")
    #list input for text
    a = ord('a')
    text = input("text\n").lower()
    textArray = list(text)
    textNum = []
    for char in textArray:
        textNum.append(ord(char)-a)
    print(textNum)
    key = input("pass\n").lower()
    keyArray = list(key)
    keyNum = []
    for char in keyArray:
        keyNum.append(ord(char)-a)
    print(keyNum)
    numList = []
    for i in range(0, len(textArray)):
        numList.append((textNum[i] + keyNum[i % len(keyNum)]) % 26)
    print(numList)
    ans = []
    for letter in numList:
        ans.append(chr(letter + a))
    print(''.join(ans))



if __name__ == '__main__':
    main()






