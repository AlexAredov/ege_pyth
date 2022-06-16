def f6(i):
    st = ''
    while i > 0:
        st = str(i % 6) + st 
        i //= 6
    return st

def f5(i):
    st = ''
    while i > 0:
        st = str(i % 5) + st 
        i //= 5
    return st

def f11(i):
    st = ''
    while i > 0:
        st = str(i % 11) + st 
        i //= 11
    return st

for i in range(0, 100):
    if len(f5(i)) == 3 and len(f6(i)) == 2 and int(f11(i))%10 == 1:
        print(i)