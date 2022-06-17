f = open('var2/27B.txt')
n = int(f.readline())

ost = [[], [], []]
for i in range(n):
    s = int(f.readline())
    ost[s % 3].append(s)
ost[0].sort()
ost[1].sort()
ost[2].sort()
print(min(ost[0][0] + ost[0][1] + ost[0][2], ost[1][0] + ost[1][1] + ost[1][2], ost[2][0] + ost[2][1] + ost[2][2], ost[0][0] + ost[1][0] + ost[2][0]))