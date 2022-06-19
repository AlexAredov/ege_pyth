def f(x, y):
    if x == y: return 1
    elif x > y or x == 33: return 0
    else:
        k = 0
        for i in range(x + 1, x + 1000):
            f1 = 0
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    f1 = 1
                    break
            if f1 == 0:
                k = i
                break
        return f(x + 2, y) + f(k, y)
print(f(2, 14) * f(14, 45))
#881