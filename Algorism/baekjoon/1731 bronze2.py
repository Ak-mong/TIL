import sys;sys.stdin=open('input.txt')
# 1731 추론
t = int(input())
arr = []
for i in range(t):
    arr.append(int(input()))
# print(arr)
flag = 3
for i in range(len(arr)):
    if i>=2 and arr[i-1] - arr[i] == arr[i-2] - arr[i-1]:
        flag = 1
    else:
        flag = 0

if flag:
    print(arr[-1] + (arr[2] - arr[1]))
else:
    print(arr[-1] * (arr[2] // arr[1]))