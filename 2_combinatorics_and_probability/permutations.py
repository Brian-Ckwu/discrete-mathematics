import itertools

if __name__ == "__main__":
    for perm in itertools.permutations("abcde", 2):
        print("".join(perm))