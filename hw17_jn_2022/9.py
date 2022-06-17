def f(x, d1, d2, d3, y):
    if x == y and d1 <= 4 and d2 >= 2 and d3 == 5: return 1
    elif x > y: return 0
    else: return f(x * 5, d1 + 1, d2, d3, y) + f(x * 3, d1, d2 + 1, d3, y) + f(x + 45, d1, d2, d3 + 1, y)
print(f(1, 0, 0, 0, 2970))
#74