import sys
# 실버 5
n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# print(arr)
arr.sort(key=lambda x: (x[1],x[0]))
# print(arr)
for i in arr:
    print(*i)