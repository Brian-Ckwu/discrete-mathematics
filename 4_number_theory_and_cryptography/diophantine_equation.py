def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

def extended_gcd(a, b):
    if b == 0:
        d, x, y = a, 1, 0
    else:
        d, p, q = extended_gcd(b, a % b)
        x = q
        y = p - (a // b) * q
    return d, x, y

def diophantine(a, b, c):
    assert c % gcd(a, b) == 0
    d, p, q = extended_gcd(a, b)
    m = c / d
    return (m * p, m * q)

if __name__ == "__main__":
    x, y = diophantine(24, 7, 3)
    print(x, y)