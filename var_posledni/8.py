s = 'АБРТЫ'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    k += 1
                    w = i1 + i2 + i3 + i4 + i5
                    if w.count('Ы') == 0 and w.count('АА') == 0:
                        print(k, w)