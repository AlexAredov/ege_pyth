k = 0
s = 'AB123'
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                w = i1 + i2 + i3 + i4
                if (w.count('A') + w.count('B') == 0):
                    k += 1
print(k)