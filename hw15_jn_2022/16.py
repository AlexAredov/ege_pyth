f = open('hw15_jn_2022/16B.txt')
l = int(f.readline())
M = 4043520
s = []
for i in range(l):
    s.append(int(f.readline()))
sd = []
for i in range(len(s)):
    if M % s[i] == 0:
        sd.append([s[i]])
        p = s[i]
        while i < (len(s) - 1) and M % (p * s[i + 1]) == 0:
            d = [k for k in sd[i]]
            d.append(s[i + 1])
            sd.append(d)
            p *= s[i + 1]
            i += 1
print(len(sd))

#A - 18
#B - 12