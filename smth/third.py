a = [i for i in range(101)]
a[0] = 1
a[1] = 1
for i in range(2,101):
    a[i] = a[i - 1] + a[i - 2]
print(a)