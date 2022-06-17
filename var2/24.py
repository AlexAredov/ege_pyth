f = open('var2/24.txt')
mina = 10000000
for i in range(990):
    s = f.readline()
    if s.count('N') < mina:
        mina = s.count('N')
        a = set(s)
        a = sorted(a)
        a.remove(a[0])
        maxa = 0
        b = ''
        for j in a:
            if s.count(j) >= maxa:
                maxa = s.count(j)
                b = j
print(b)