k = 0
for i in range(245690, 245756):
    k+=1
    c = 0
    for j in range(2, i - 1):
        if i % j == 0:
            c += 1
            break
    if c == 0:
        print(k, i)