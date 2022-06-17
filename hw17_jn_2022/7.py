m = []
def f(x, d):
    if d == 9:
        if x > 0 and x not in m:
            m.append(x)
    else:
        f(x - 3, d + 1)
        f(x * (-3), d + 1)
f(133, 0)
print(len(m))
#191