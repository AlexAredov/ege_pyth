f = open('hw17_jn_2022/18B.txt')
n = int(f.readline())
s = f.readlines()
for i in range(n):
    s[i] = int(s[i])
k = []
for n in range(n):
    f = 0
    for i in range(2, int(s[n]**0.5) + 1):
        if s[n] % i == 0:
            f = 1
            break
    if f == 0:
        k.append(s[n])
#print(k)
print(len(k))
if len(k) % 9 != 0:
    summ1 = k[len(k) % 9 - 1]
    for i in range(0, s.index(k[len(k) % 9 - 1])):
        summ1 += s[i]
    summ2 = k[-(len(k) % 9)]
    for i in range(len(s) - 1, len(s) - s[::-1].index(k[-(len(k) % 9)]) - 1, -1):
        summ2 += s[i]
    print(summ1, summ2)
    summ = 0
    for i in range(0, len(s)):
        summ += s[i]
    print(summ)
    if summ1 > summ2:
        summ -= summ2
        print(summ)
    else:
        summ -= summ1
        print(summ)