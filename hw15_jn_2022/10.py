def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else: return f(x + 3, y) + f(x * 3, y)
k = 0
for i in range(4, 100, 2):
    s = f(3, i)
    if s != 0:
        k += 1
print(k)
#12