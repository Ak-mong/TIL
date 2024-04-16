import sys
input = sys.stdin.readline
# 26099 설탕 배달 2 실버4
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))
# print(n,m)
dicts = {}
for i in range(n):
    dicts.setdefault(arr[i], 0)

    if dicts[arr[i]]:
        dicts[arr[i]] += 1
    else:
        dicts[arr[i]] = 1
for j in find:
    if j in dicts.keys():
        print(dicts[j], end=' ')
    else:
        print(0, end=' ')
