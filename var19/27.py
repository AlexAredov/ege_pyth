f = open('var19/27A.txt')
n = int(f.readline())

summ = 0
a = []
for i in range(n):
    s = f.readline().split(' ')
    summ += min(int(s[0]), int(s[1]))
    a.append([min(int(s[0]), int(s[1])), max(int(s[0]), int(s[1]))])
print(summ)
a.sort()
print(a)
i = 0
while summ % 59 == 0:
    summ -= min(a[-i])
    summ += max(a[-i])
    i += 1
print(summ)