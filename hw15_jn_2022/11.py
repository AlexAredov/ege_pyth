def f(x, d, y):
    if x == y: return d
    elif x > y or d > 5: return 1000000
    else:
        if x % 4 != 0:
            return min(f(x + 1, d + 1, y), f(x * 2, d + 1, y), f(x + (x % 4), d + 1, y))
        else:
            return min(f(x + 1, d + 1, y), f(x * 2, d + 1, y))
k = 0
for i in range(1, 81):
    if f(i, 0, 80)<= 5:
        k += 1
print(k)
#34