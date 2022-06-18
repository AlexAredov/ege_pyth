def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else:
        if x % 2 != 0:
            return f(x + 2, y) + f(x + 3, y) + f(2 * x, y)
        else:
            return f(x + 2, y) + f(x + 3, y)
print(f(3, 46))
#126801