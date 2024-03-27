import sys
# 1009 분산처리 브2

t = int(sys.stdin.readline())
for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a == 1 or a== 5 or a == 6:
        print(a)
    elif a  == 4 or a == 9:
        b %= 2
        if b == 1:
            print(a)
        else:
            print(a**2 % 10)
    else: # 2,3,7,8
        b %= 4
        if b ==0:
            print(a ** 4 % 10)
        else:
            print(a ** (b%4) % 10)