"""
    Finding the solutions to the N Queens problem (place n queens on a n*n chess board):
        1. Brute-force search
        2. Backtracking
"""

import itertools

# 1. Brute-force search
def is_solution(perm: tuple) -> bool:
    for i1, i2 in itertools.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True

def brute_force_search(n: int) -> list:
    solutions = list()
    for perm in itertools.permutations(range(n)):
        if is_solution(perm):
            solutions.append(perm)
    return solutions

if __name__ == "__main__":
    n = 8
    solutions = brute_force_search(n)
    for sol in solutions:
        print(sol)