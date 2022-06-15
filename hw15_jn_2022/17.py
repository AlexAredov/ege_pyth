f = open('hw15_jn_2022/17A.txt')
l = int(f.readline())
maxa = 0

k = f.readlines()
for i in range(len(k)):
    k[i] = int(k[i])

sd = []
for i in range(len(k)):
    summ = 0
    for j in range(i, len(k)):
        summ = summ + k[j]
        if summ % 93 == 0 and summ % 2 != 0:
            sd.append(summ)
print(max(sd))

#A - 22227
#B - ???