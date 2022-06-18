for A in range(0,10):
    for x in range(0,100):
        f = 0
        if ((x & 46 != 0) <= ((x & 42 == 0) <= (x & A != 0))) == 0:
            f = 1
            break
    if f == 0:
        print(A)