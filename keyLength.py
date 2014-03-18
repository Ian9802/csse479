print("key length")
text = input()
text = text.lower()
textArray = list(text)

def collisions(list, offset):
    count = 0
    for i in range(offset, len(list)):
        if list[i] == list[i-offset]:
            count += 1
    return count

coincidences = list()
for i in range(1, len(textArray)):
    coincidences.append((collisions(textArray, i), i))

keys = sorted(coincidences)
keys.reverse()
print(keys)
