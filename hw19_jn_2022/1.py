s = 'АИКЛМЬ'
a = []
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        w = i1 + i2 + i3 + i4 + i5 + i6
                        a.append(w)
for i in range(len(a)):
    #print(a[i][0])
    if a[i][0] == 'К' and a[i][-1] == 'Ь':
        if len(set(a[i])) == 6:
            if a.index(a[i][::-1]) - i == 26655:
                #print(a.index(a[i][::-1]), a[a.index(a[i][::-1])])
                print(i, a[i])
#16475