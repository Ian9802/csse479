text = input()
text = text.lower()
textArray = list(text)
cypher = input()
cypher = cypher.lower()
cypherArray = list(cypher)


def adjust(list, cypher):
    RL = []
    a = ord('a')
    for i in range(0, len(list)):
        c = ord(list[i]) - a
        s = ord(cypher[i % len(cypher)]) - a
        RL.append(chr(((c-s) % 26) + a))
    return RL

print(''.join(adjust(textArray, cypherArray)))