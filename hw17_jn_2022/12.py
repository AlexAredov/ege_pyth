k = 0
for n in range(400000000, 400000100):
    dl = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and i**2 != n:
            dl.append(i)
            dl.append(n//i)
        if i**2 == n:
            dl.append(i)
    if len(dl) > 7:
        k += 1
        dl.sort(reverse=True)
        print(dl[7],len(dl))
    if k == 5:
        break