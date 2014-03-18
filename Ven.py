text = input()
text = text.lower()
textArray = list(text)
cypher = input()
cypher = text.lower()
cypherArray = list(text)

def adjust(list, cypher):
    RL = []
    a = ord('a')
    for i in range(0, len(list)):
        c = ord(list[i])
        s = ord(cypher[i%len(cypher)])
        RL.append(chr(((c-a+s-a) % 26) + a))
    return RL

print(''.join(adjust(textArray, cypherArray)))