def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else: return f(x + 3, y) + f(x * 3, y)
k = 0
sd = []
for i in range(4, 100):
    s = f(3, i)
    if s != 0 and s not in sd:
        k += 1
        sd.append(s)
print(len(sd))
#12