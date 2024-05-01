import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

#2751 실버 5 수 정렬하기 2
n = int(input())
arr = []
for i in range(n):
    value = int(input())
    arr.append(value)
    # print(arr)
arr.sort()
for k in arr:
    print(k)