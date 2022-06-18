f = open('var19/24.txt')
s = f.readline()
k = 0
for i in range(len(s) - 1):
    if s[i] + s[i + 1] == 'XV':
        k += 1
print(k)