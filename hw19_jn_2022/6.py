f = open('hw19_jn_2022/6.txt')
sd = []
s = f.readline()
for i in range(len(s) - 1):
    if s[i] == 'X':
        f = 0
        for n in range(len(sd)):
            if sd[n][1] == s[i + 1]:
                f = 1
                sd[n][0] += 1
                break
        if f == 0:
            sd.append([0, s[i + 1]])
sd.sort()
print(sd[-1][1], sd[-1][0])
#U 1617