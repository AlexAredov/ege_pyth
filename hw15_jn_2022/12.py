k = 0
m = 0
maxa = 0
for l in range(238941, 315675):
    n = l
    dl = []
    d = 2
    while d * d <= n:
        if n % d == 0 and d**2 != n:
            dl.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        dl.append(n)
    print(l, dl)
    if len(dl) == 2:
        if dl[0]**2 != n:
            k += 1
            if max(dl) - min(dl) > maxa:
                maxa = max(dl) - min(dl)
                m = n
print(k, m)
#16386 157837