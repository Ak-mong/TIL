import sys
input = sys.stdin.readline

# 11931 수 정렳하기 4 실버5
n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
arr.sort(reverse=True)
# print(arr)
for i in arr:
    print(i)