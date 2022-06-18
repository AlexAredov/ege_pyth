for x in range(100, 300):
    L = x
    M = 77
    if L % 2 == 0:
        M = 32
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 16:
        print(x)