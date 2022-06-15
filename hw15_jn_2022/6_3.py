def f(s, h, n):
    if s >= 20:
        if n % 2 == 0: return True
        else: return False
    else:
        if n % 2 == 0:
            if h == 0:
                return f(s + 2, h, n + 1) and f(s * 2, h, n + 1) and f(s, 1, n + 1)
            else:
                return f(s + 2, h, n + 1) and f(s * 2, h, n + 1)
        else:
            if h == 0:
                return f(s + 2, h, n + 1) or f(s * 2, h, n + 1) or f(s, 1, n + 1)
            else:
                return f(s + 2, h, n + 1) or f(s * 2, h, n + 1)
for s in range(1, 20):
    if f(s, 0, 0):
        print(s)
#1 7