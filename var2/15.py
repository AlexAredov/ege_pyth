sd = []
for Amin in range(0,99):
    for Amax in range(Amin, 100):
        A = [i for i in range(Amin, Amax)]
        f = 0
        for x in range(0,100):
            if (((x in A) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in A))) == 0:
                f = 1
        if f == 0:
            sd.append(len(A))
print(max(sd))