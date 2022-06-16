def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else:
        if x % 2 == 0:
            return f(x + 1, y) + f(x * 2, y) + f(x + 1, y)
        else:
            return f(x + 1, y) + f(x * 2, y) + f(x + 2, y)
print(f(3, 9) * f(9, 17) * f(17, 25))
#229635