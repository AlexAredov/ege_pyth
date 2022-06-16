for l in range(100000, 500000):
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
    if len(dl) > 3:
        dd = dl[1] - dl[0]
        f = 0
        for i in range(len(dl) - 1):
            if dl[i + 1] - dl[i] != dd:
                f = 1
                break
        if f == 0 and dd != 0:
            print(l, len(dl) * dd)
#101065 48
#124729 24
#177289 48
#278185 72