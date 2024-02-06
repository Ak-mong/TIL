def itoa(a):
    s = ''
    while a >0:
        s = chr(a%10 + ord('0')) + s
        a //= 10
    return s

ans = itoa(123)
print(ans)
print(type(ans))