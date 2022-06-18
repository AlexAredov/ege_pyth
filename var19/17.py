f = open('var19/17.txt')
a = []
for i in range(0, 6000):
    s = int(f.readline())
    a.append(s)
k = 0
sum_max = 0
for i in range(len(a) - 2):
    if a[i] > 0 or a[i + 1] > 0 or a[i + 2] > 0:
        k += 1
        if (a[i] + a[i + 1] + a[i + 2]) > sum_max:
            sum_max = a[i] + a[i + 1] + a[i + 2]
print(k, sum_max)