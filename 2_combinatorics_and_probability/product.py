import itertools as it

if __name__ == "__main__":
    for prod in it.product(range(3), repeat=3):
        print(prod)