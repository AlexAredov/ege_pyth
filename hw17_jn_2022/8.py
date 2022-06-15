def f(x, d, y):
    if x == y: return d
    elif x > y or d > 3: return 10000000
    else:
        if x % 6 == 0:
            return min(f(x + 2, d + 1, y), f(x * 2, d + 1, y), f(x * 3, d + 1, y))
        else:
            return min(f(x + 2, d, y), f(x * 2, d, y), f(x * 3, d, y))
if f(1, 0, 300) <= 3:
    print(f(1, 0, 300))
#???