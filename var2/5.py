def f(i):
    st = ''
    while i > 0:
        st = str(i % 2) + st 
        i //= 2
    k = int(st) - 10**(len(st) - 1)
    return int(str(k), base=2)
sd = []
for i in range(10, 1001):
    sd.append(i - f(i))
sd = set(sd)
print(len(sd))