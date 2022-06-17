k = 0
for i in range(452021, 453000):
    sd = []
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0 and j**2 != i:
            sd.append(j)
            sd.append(i//j)
            break
    M = sum(sd)
    if M % 7 == 3:
        k += 1
        print(i, M)
    if k == 5:
        break