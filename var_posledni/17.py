f = open('var_posledni/17.txt')
sd = []
for i in range(0,10000):
    s = int(f.readline())
    sd.append(s)
mina = max(sd)
for i in range(len(sd)):
    if sd[i] < mina and sd[i] % 21 == 0:
        mina = sd[i]
#print(mina)
maxa = 0
k = 0
for i in range(len(sd) - 1):
    if sd[i] % mina == 0 or sd[i + 1] % mina == 0:
        k += 1
        summ = sd[i] + sd[i + 1]
        if summ > maxa:
            maxa = summ
print(k, maxa)