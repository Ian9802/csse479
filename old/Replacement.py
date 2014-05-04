def main():
    text = input("text\n")
    text = text.lower()
    textArray = list(text)
    singles = sorted(getSet(textArray, 1))
    doubles = sorted(getSet(textArray, 2))
    triples = sorted(getSet(textArray, 3))
    singles.reverse()
    doubles.reverse()
    triples.reverse()
    print(singles)
    print(doubles)
    print(triples)


def getSet(text, size):
    returnSet = []
    returnValues = []
    for i in range(0, len(text)-size):
        val = []
        for j in range(i, size+i):
            val.append(text[j])
        setValue = ''.join(val)
        if setValue in returnSet:
            returnValues[returnSet.index(setValue)] += 1
        else:
            returnSet.append(setValue)
            returnValues.append(1)
    result = []
    for i in range(0, len(returnSet)):
        result.append((returnValues[i], returnSet[i]))
    return result


def getSingles(text):
    returnLetters = []
    returnValues = []
    for letter in text:
        if letter in returnLetters:
            i = returnLetters.index(letter)
            returnValues[i] += 1
        else:
            returnLetters.append(letter)
            returnValues.append(1)
    result = []
    for i in range(0, len(returnLetters)):
        result.append((returnValues[i], returnLetters[i]))
    return result


def getDoubles(text):
    returnPairs = []
    returnValues = []
    for i in range(0, len(text)-1):
        pair = text[i] + text[i+1]
        if pair in returnPairs:
            i = returnPairs.index(pair)
            returnValues[i] += 1
        else:
            returnPairs.append(pair)
            returnValues.append(1)
    result = []
    for i in range(0, len(returnPairs)):
        result.append((returnValues[i], returnPairs[i]))
    return result

def getTriples(text):
    returnTriples = []
    returnValues = []
    for i in range(0, len(text)-2):
        pair = text[i] + text[i+1] + text[i+2]
        if pair in returnTriples:
            i = returnTriples.index(pair)
            returnValues[i] += 1
        else:
            returnTriples.append(pair)
            returnValues.append(1)
    result = []
    for i in range(0, len(returnTriples)):
        result.append((returnValues[i], returnTriples[i]))
    return result


if __name__ == '__main__':
    main()