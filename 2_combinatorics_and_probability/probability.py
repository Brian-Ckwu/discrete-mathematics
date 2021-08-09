from time import perf_counter

def execution_time(func, *args):
    start = perf_counter()
    res = func(*args)
    end = perf_counter()
    return res, end - start

def c(n: int, k: int) -> int:
    p = 1
    k_fac = 1
    for i in range(k):
        p *= n - i
        k_fac *= k - i
    return int(p / k_fac)

def galton_board_naive(low: int, high: int, n: int) -> float:
    pr = 0
    base = 2 ** n
    for i in range(low, high + 1):
        pr += c(n, i) / base
    return pr

def galton_board_fast(low: int, high: int, n: int) -> float:
    def fac(k: int) -> int:
        prod = 1
        for i in range(1, k + 1):
            prod *= i
        return prod
    nu = fac(n)
    de = fac(low) * fac(n - low)
    base = 2 ** n
    pr = (nu / de) / base
    for i in range(1, high - low + 1):
        de *= (low + i) / (n - low + 1 - i)
        pr += (nu / de) / base
    return pr

if __name__ == "__main__":
    low, high, n = 40, 60, 100
    pr1, exec_time1 = execution_time(galton_board_naive, low, high, n);
    pr2, exec_time2 = execution_time(galton_board_fast, low, high, n);
    print(f"Naive -> res: {pr1} / runtime: {exec_time1}")
    print(f"Fast -> res: {pr2} / runtime: {exec_time2}")