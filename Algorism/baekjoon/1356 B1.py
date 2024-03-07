import sys;sys.stdin = open('input.txt')

n = list(map(int,input()))
lens = len(n)
flag = 0
for i in range(lens):
    for j in range(i+1,lens):
        a = n[0:j]
        b = n[j:lens]
        # print(a,b)
        multi_a = 1
        multi_b = 1
        for x in range(len(a)):
            multi_a *= a[x]
        for y in range(len(b)):
            multi_b *= b[y]
        # print(multi_a, multi_b)
        if multi_a == multi_b:
            flag = 1
if flag:
    print('YES')
else:
    print('NO')