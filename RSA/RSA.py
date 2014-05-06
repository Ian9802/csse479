__author__ = 'Ian'


def main():
    c = 47386274600715627711741231320889953635052682912275895170705519441900467437234068120729231868997125356903089949357565563350604020398667889098417715800228490969143071606844546349141649145365269219264564662542369533624712494
    n = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000973
    e = 5
    p = ((10 ** 110) + 7)
    q = ((10 ** 111) + 139)
    pq = (p - 1) * (q - 1)
    d = getD(e, pq)
    m = power(c, d, n)
    numString = "" + str(m)
    if len(numString) % 3 == 0:
        message = text(numString)
    elif len(numString) % 3 == 1:
        message = text("00" + numString)
    else:
        message = text("0" + numString)
    print("".join(message))


def getD(e, pq):
    b = 1
    gcd, t, s = euclid(e, pq)
    return t*b % pq


def euclid(b, a):
    #reference: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    s = 1
    sP = 0
    t = 0
    tP = 1
    while b != 0:
        q = a // b
        r = a % b
        sPP = s - q * sP
        tPP = t - q * tP
        a = b
        b = r
        s = sP
        sP = sPP
        t = tP
        tP = tPP
    gcd = a
    return gcd, t, s


def power(c, d, n):
    if d < 15:
        return (c ** d) % n
    exp = 1
    #for the life of me I cant remember if it's multC for multiplying c or multi-count
    multC = c
    while exp < d / 2:
        multC *= multC
        multC %= n
        exp *= 2
    multC = (multC * power(c, (d - exp), n)) % n
    return multC


def translate(char):
    return chr(int(char))


def text(numString):
    letters = []
    for x in range(0, len(numString)//3):
        temp = ""
        for y in range(0, 3):
            temp += numString[(x*3)+y]
        letters.append(translate(temp))
    return letters


if __name__ == '__main__':
    main()