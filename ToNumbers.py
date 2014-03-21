text = input("text\n").lower()
a = ord('a')
out = list(text)
allOut = []
for letter in out:
    allOut.append(ord(letter)-a)
print(allOut)