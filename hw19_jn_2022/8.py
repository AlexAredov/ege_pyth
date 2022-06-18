import math
for n in range(99999, 1048571):
    if int(math.log2(n)) == math.log2(n):
        for i in range(-5, 6):
            c = n + i
            f = 0
            for j in range(2, int(c**0.5) + 1):
                if c % j == 0:
                    f = 1
            if f == 0:
                print(c, n)
#131071 131072
#262139 262144
#262147 262144
#524287 524288