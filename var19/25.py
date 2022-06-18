k = 0
for n in range(650000, 700000):
    sd = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and i**2 != n:
            f = 0
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    f = 1
            if f == 0:
                sd.append(i)
            f = 0
            for j in range(2, int((n//i)**0.5) + 1):
                if (n//i) % j == 0:
                    f = 1
            if f == 0:
                sd.append(n//i)
        if i**2 == n:
            f = 0
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    f = 1
            if f == 0:
                sd.append(i)
    if sum(sd) % 10 == 5:
        print(n, sum(sd))
        k += 1
    if k == 5:
        break