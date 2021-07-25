"""
    Finding the solutions to the N Queens problem (place n queens on a n*n chess board):
        1. Brute-force search
        2. Backtracking
"""

import itertools

# 1. Brute-force search
# Time complexity: O(n^2) (n == length of perm)
def is_solution(perm: tuple) -> bool:
    for i1, i2 in itertools.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True

# Time complexity: O(n^2 * n!)
def brute_force_search(n: int) -> list:
    solutions = list()
    for perm in itertools.permutations(range(n)): # O(n!)
        if is_solution(perm): # O(n^2)
            solutions.append(perm)
    return solutions

# 2. Backtracking method
def is_sub_solution(sub_sol: list) -> bool:
    for i1, i2 in itertools.combinations(range(len(sub_sol)), 2):
        if abs(i1 - i2) == abs(sub_sol[i1] - sub_sol[i2]):
            return False
    return True

def extend(perm: list, n: int, solutions: list) -> None:
    if len(perm) == n:
        solutions.append(perm)
    # extend the permutation
    for i in range(n):
        if i not in perm:
            perm.append(i)
            if is_sub_solution(perm):
                extend(perm, n, solutions)
            perm.pop()

def back_track_search(n: int) -> list:
    solutions = []
    extend(perm=[], n=n, solutions=solutions)
    return solutions


if __name__ == "__main__":
    max_n = 10
    for i in range(1, max_n + 1):
        solutions = back_track_search(i) # much faster than brute_force_search
        print(f"The number of solutions of n={i}: {len(solutions)}")