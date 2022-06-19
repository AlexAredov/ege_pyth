s = '8'*84
while ('1111' in s) or ('8888' in s):
    if '1111' in s:
        s = s.replace('1111', '8')
    else:
        s = s.replace('8888', '11')
print(s)