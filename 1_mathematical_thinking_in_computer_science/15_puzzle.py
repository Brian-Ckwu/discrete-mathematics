def is_permutation(perm: list) -> bool:
    return set(perm) == set(range(len(perm)))

def is_even_permutation(perm: list) -> bool:
    swaps = 0
    for i in range(len(perm)):
        if (perm[i] == i):
            continue
        while (perm[i] != i):
            temp = perm[i]
            perm[i] = perm[perm[i]]
            perm[temp] = temp
            swaps += 1
    return swaps % 2 == 0

if __name__ == "__main__":
    perm = [0,3,2,4,5,6,7,1,9,8]
    print(is_even_permutation(perm))
    print(perm)