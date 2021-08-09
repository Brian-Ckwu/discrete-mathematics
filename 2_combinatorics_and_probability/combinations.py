from tqdm import tqdm
import itertools
import math

def demo_comb() -> None:
    for c in itertools.combinations("abcde", 2):
        print("".join(c))
    
def comb_by_pascal(n: int, k: int) -> int:
    c = dict() # dictionary for pascal triangle
    # initialization
    for i in tqdm(range(n + 1)): # fill the pascal triangle row by row
        c[(i, 0)] = 1
        for j in range(1, i):
            c[(i, j)] = c[(i - 1, j - 1)] + c[(i - 1, j)]
        c[(i, i)] = 1
    return c[(n, k)]

def c(n: int, k: int) -> int:
    p = 1
    k_fac = 1
    for i in range(k):
        p *= n - i
        k_fac *= k - i
    return int(p / k_fac)

def binomial_coefficients(a: int, b: int, n: int) -> list:
    coefs = list()
    for i in range(n + 1):
        coef = c(n, i) * a**(n - i) * b**(i)
        coefs.append(coef)
    return coefs

if __name__ == "__main__":
    print(c(6, 3) * (5**3)**2)