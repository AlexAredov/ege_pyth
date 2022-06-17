i = int(input())
s = ''
while i > 0:
    s = str(i % 2) + s
    i //= 2
print(s)