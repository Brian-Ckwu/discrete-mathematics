def gcd(a: int, b: int) -> int:
    assert a >= 0 and b >= 0
    return gcd(b, a % b) if b != 0 else a

def extended_gcd(a: int, b: int) -> tuple:
    assert a >= 0 and b >= 0
    # compute d, x, y
    if b == 0:
        d, x, y = a, 1, 0
    else:
        d, p, q = extended_gcd(b, a % b)
        x = q
        y = p - (a // b) * q
    # check answers
    assert d == a * x + b * y
    return (d, x, y)

if __name__ == "__main__":
    res = extended_gcd(24, 7)
    print(res)