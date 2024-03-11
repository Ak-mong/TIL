import sys;sys.stdin=open('input.txt')
# 1292 쉽게 푸는 문제
a,b = map(int,input().split())
arr = [0] * 1001 # 천이하의 수이기 때문
i = 1
j = 1
flag = 1
while flag:
    for _ in range(i):
        if j == 1001:
            flag = 0
            break
        arr[j] = i
        j += 1

    if not flag:
        break
    i += 1

# print(arr)
sum_v =0
for i in range(a,b+1):
    sum_v += arr[i]
print(sum_v)