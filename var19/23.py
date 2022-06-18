def f(x, y):
    if x == y: return 1
    elif x > y or x == 29: return 0
    else: return f(x + 1, y) + f(x * 3, y)
print(f(2, 10) * f(10, 33))