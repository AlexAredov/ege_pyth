m = []
def f(x, d):
    if d == 5:
        if x not in m:
            m.append(x)
    else:
        f(x + 2, d + 1)
        f(x + 3, d + 1)
        f(x * 2, d + 1)
f(10, 0)
print(len(m))
#83