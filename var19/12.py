s = '1122'*71
while '12' in s or '222' in s:
    if '12' in s:
        s = s.replace('12', '2')
    else:
        s = s.replace('222', '2')
print(s)