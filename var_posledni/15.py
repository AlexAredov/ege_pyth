for A in range(1, 10000):
    f = 0
    for x in range(1, 10000):
        if (((x % 3 == 0) <= (x % 5 != 0)) or (x + A >= 90)) == 0:
            f = 1
            break
    if f == 0:
        print(A)
        break