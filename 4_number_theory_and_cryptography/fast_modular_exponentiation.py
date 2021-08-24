# for testing decimal to binary representation
def to_binary_rep(n: int) -> list:
    b = list()
    while n:
        r = n % 2
        n = n // 2
        b.append(r)
    return list(reversed(b))

def FastModularExponentiationK(b, k, m):
    res = b % m
    for _ in range(k):
        res = (res * res) % m
    return res

def FastModularExponentiationE(b, e, m):
    res = 1
    cur = b
    while e:
        r = e % 2
        e = e // 2
        if r == 1:
            res = (res * cur) % m
        cur = cur**2 % m # cur: b^(2^k), k == ith iteration (cur for the (i+1)th iteration)
    return res

if __name__ == "__main__":
    print(FastModularExponentiationK(2, 3, 7))
    print(FastModularExponentiationE(2, 10, 7))
