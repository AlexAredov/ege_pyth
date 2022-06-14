def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else:
        if x % 3 == 0:
            return f(x + 1, y) + f(int(str(x) + '1'), y) + f(x * 5, y)
        else:
            return f(x + 1, y) + f(x * 5, y)
print(f(1, 140))
#111