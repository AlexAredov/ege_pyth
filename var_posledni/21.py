def f(s1, s2, n):
    if s1 + s2 >= 231:
        if n == 2 or n == 4: return True
        else: return False
    else:
        if n >= 4: return False
        elif n % 2 == 0: return f(s1 + 1, s2, n + 1) and f(s1 * 2, s2, n + 1) and f(s1, s2 + 1, n + 1) and f(s1, s2 * 2, n + 1)
        else: return f(s1 + 1, s2, n + 1) or f(s1 * 2, s2, n + 1) or f(s1, s2 + 1, n + 1) or f(s1, s2 * 2, n + 1)

def f1(s1, s2, n):
    if s1 + s2 >= 231:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0: return f1(s1 + 1, s2, n + 1) and f1(s1 * 2, s2, n + 1) and f1(s1, s2 + 1, n + 1) and f1(s1, s2 * 2, n + 1)
        else: return f1(s1 + 1, s2, n + 1) or f1(s1 * 2, s2, n + 1) or f1(s1, s2 + 1, n + 1) or f1(s1, s2 * 2, n + 1)


for s in range(1, 214):
    if f(17, s, 0) and not(f1(17,s,0)):
        print(s)