def f(x, d, y):
    if x == y: return d
    elif x < y or d > 9: return 1000000
    else:
        return min(f(x - 3, d + 1, y), f(x * (-3), d + 1, y))
k = 0
for i in range(132, 0, -1):
    #print(133, i, f(133, 0, i))
    if f(133, 0, i) == 9:
        k += 1
print(k)