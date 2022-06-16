f = open('hw17_jn_2022/13.txt')
n = f.readline().split(' ')
x = int(n[0])
y = int(n[1])
n = int(n[2])
print(x, y, n)
data = []
for i in range(n):
    s = f.readline().split(' ')
    data.append([int(s[0]), int(s[1])])
data.sort()
for i in range(1,y):
    l = 0
    for j in range(0, len(data)):
        if data[j][0] == i:
            l = j
            break
    a = []
    while data[l][0] == i:
        a.append(data[l][1])
        l+=1
    dl = []
    for j in range(len(a) - 1):
        dll = 0
        if a[j + 1] - a[j] >= 4:
            dll += a[j + 1] - a[j] - 4 + 1
    dl.append([dll, i])
    #print(l,a)
print(dl[0][0], dl[0][1])