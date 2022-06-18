i = 4**500 + 3*(4**2500) + 16**500 - 1024
s = ''
while i > 0:
    s = str(i % 4) + s
    i //= 4
print(s.count('3'))