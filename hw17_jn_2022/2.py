def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else: return f(x + 1, y) + f(int(str(x) + '1'), y)
print(f(1, 555))
#181