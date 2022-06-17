from turtle import back


k = 0
for l in range(121332132, 20222021, -1):
    n = l
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
            print(l, dl[0])
    if k == 5:
        break
#121332131 8963
#121332097 3347
#121332053 1291
#121332037 4481
#121332031 1741