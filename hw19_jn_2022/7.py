for n in range(1, 1000000, 1):
    if n % 103 == 0:
        s = str(n)
        f = 0
        for i in range(len(s) - 1):
            if int(s[i]) >= int(s[i + 1]):
                f = 1
                break
        if f == 0:
            print(n, n//103)
#1236 12
#2369 23
#2678 26
#16789 163