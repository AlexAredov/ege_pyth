s = 'АЕЖЙМУ'
k = 0
l = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    k += 1
                    if k % 2 == 0:
                        w = i1 + i2 + i3 + i4 + i5
                        if (('АА'  not in w) and ('ЕЕ'  not in w)
                        and ('ЖЖ'  not in w) and ('ЙЙ'  not in w)
                        and ('ММ'  not in w) and ('УУ'  not in w)):
                            l += 1
print(l)
#360?