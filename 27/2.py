f = open('27/2B.txt')
n = int(f.readline())
mina = 10000000
summa = 0
for i in range(0, n):
    s = f.readline().split()
    a1 = max(int(s[0]), int(s[1]))
    a2 = min(int(s[0]), int(s[1]))
    summa += a2
    if ((a1 - a2) < mina) and ((a1 - a2) % 3 != 0):
        mina = a1 - a2
if summa % 3 == 0:
    summa += mina
print(summa)