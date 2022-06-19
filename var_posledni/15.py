for A in range(0, 1000):
    f = 0
    for x in range(0, 100):
        if (((x % 3 == 0) <= (not(x % 5 == 0))) or (x + A >= 90)) == 0:
            f = 1
            break
    if f == 0:
        print(A)