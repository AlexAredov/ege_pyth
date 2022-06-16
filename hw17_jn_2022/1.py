s = 'АЕПСТУХ'
k = 0
l = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                l += 1
                w = i1 + i2 + i3 + i4
                if l > 1000:
                    if (('АА' not in w) and ('ЕЕ' not in w)
                    and ('ПП' not in w) and ('СС' not in w)
                    and ('ТТ' not in w) and ('УУ' not in w)
                    and ('ХХ' not in w)):
                        k += 1
print(k)
#883