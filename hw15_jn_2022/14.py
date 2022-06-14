for n in range(12034679, 23175821):
    if (n**0.25) == int(n**0.25):
        f = 0
        for i in range(2, int((int(n**0.25))**0.5) + 1):
            if (int(n**0.25)) % i == 0:
                f = 1
                break
        if f == 0:
            print(n, int(n//(n**0.5)))

#12117361 3481
#13845841 3721
#20151121 4489