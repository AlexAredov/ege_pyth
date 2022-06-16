s = 'МАТВЕЙ'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        w = i1 + i2 + i3 + i4 + i5 + i6
                        if len(set(w)) == 6:
                            if i1 != 'Й' and 'АЕ' not in w:
                                k += 1
print(k)