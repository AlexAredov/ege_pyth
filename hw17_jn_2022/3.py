def f(x, h, y):
    if x == y: return 1
    elif x > y: return 0
    else: 
        if h == 0:
            return f(x + 1, 1, y) + f(x + 3, 0, y) + f(x * 2, 0, y)
        else:
            return f(x + 3, 0, y) + f(x * 2, 0, y)
print(f(3, 0, 30))