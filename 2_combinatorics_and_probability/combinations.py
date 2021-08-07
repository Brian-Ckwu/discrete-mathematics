from tqdm import tqdm
import itertools

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

if __name__ == "__main__":
    n = 4000
    k = 3
    print(comb_by_pascal(n, k))