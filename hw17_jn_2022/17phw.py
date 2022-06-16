f = open('hw17_jn_2022/17B.txt')
n = int(f.readline())

s = 0
list_sum = [-1]*93
list_sum[0] = 0
max_sum = 0
for i in range(n):
    a = int(f.readline())
    s += a
    ost = s % 93
    if list_sum[ost] != -1:
        new_sum = s - list_sum[ost]
        if new_sum > max_sum and new_sum % 2 != 0:
            max_sum = new_sum
    else:
        list_sum[ost] = s
print(max_sum)