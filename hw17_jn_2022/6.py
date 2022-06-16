def f(x, h, y):
    if x == y: return 1
    elif x > y or x == 12 or x == 20: return 0
    else:
        if h == 0:
            return f(x + 1, 0, y) + f(x + 2, 0, y) + f(x * 3, 1, y)
        else:
            return f(x + 1, 0, y) + f(x + 2, 0, y)
print(f(2, 0, 15) * f(15, 0, 30) * f(30, 0, 38))
#1243550