def gcd(a, b):
    assert a >= 0 and b >= 0
    return gcd(b, a % b) if b != 0 else a

if __name__ == "__main__":
    d = gcd(24, 16)
    print(d)