from re import T


def f(s1, s2, n):
    if s1 + s2 >= 100:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0: return f(s1 + 5, s2, n + 1) or f(s1**2, s2, n + 1) or f(s1, s2 + 5, n + 1) or f(s1, s2**2, n + 1)
        else: return f(s1 + 5, s2, n + 1) or f(s1**2, s2, n + 1) or f(s1, s2 + 5, n + 1) or f(s1, s2**2, n + 1)
for s in range(1, 96):
    if f(3, s, 0):
        print(s)