def f(x, d1, d2, d3, y):
    if x == y and d1 <= 5 and d2 <= 2 and d3 == 5: return 1
    elif x > y or d1 > 5 or d2 > 2 or d3 != 5: return 0
    else: return f(x * 5, d1 + 1, y) + f(x * 3, d2 + 1, y) + f(x + 45, d3 + 1, y)
print(f(1, 0, 0, 0, 2970))
#0