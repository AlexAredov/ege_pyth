def f(n):
    if n == 1: return 1
    elif n % 2 == 0: return n + 2*f(n - 1)
    elif (n > 1) and (n % 2 != 0): return 2**n + f(n - 2)
print(f(16))