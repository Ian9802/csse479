__author__ = 'Ian'

def main():
    print(problem6())

def problem4():
    return (modular_inverse(314, 11111)*271) % 11111


def modular_inverse(value, mod):
    gcd, x, y = extended_euclidean(value, mod)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % mod


def extended_euclidean(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def problem5():
    for i in range(1, 10000):
        if (2 ** i)%391 == 1:
            return i

def problem6():
    values = {}
    for i in range(1, 65537):
        x = (3**i) % 65537
        if x in values:
            return False
        else:
            values[x] = True
    return True


def p61():
    for i in range(0, 65537):
        if (3 ** i)%65537 == 1:
            return i

if __name__ == '__main__':
    main()