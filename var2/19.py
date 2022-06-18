def f(s1 , s2, n):
    if s1 + s2 <= 40:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0: return f(s1 - 1, s2, n + 1) or f(s1, s2 - 1, n + 1) or f((s1//2) + s1%2, s2, n + 1) or f(s1, (s2//2) + s2%2, n + 1)
        else: return f(s1 - 1, s2, n + 1) or f(s1, s2 - 1, n + 1) or f((s1//2) + s1%2, s2, n + 1) or f(s1, (s2//2) + s2%2, n + 1)
for s in range(21, 100):
    if f(20, s, 0):
        print(s)