k = 0
for n in range(400000001, 400000100):
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
        print(dl[6],len(dl))
    if k == 5:
        break
#16000000 97
#17 10
#135 14
#921659 30
#16666667 62