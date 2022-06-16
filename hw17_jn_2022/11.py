from turtle import back


k = 0
for n in range(121332132, 20222022, -1):
    l = n
    dl = []
    d = 2
    while d*d <= n:
        if n % d == 0 and d**2 != n:
            dl.append(d)
            n //= d
            break
        else:
            d += 1
    if len(dl) > 0:
        if dl[0] > 999:
            k += 1
            print(n, dl[0])
    if k == 5:
        break