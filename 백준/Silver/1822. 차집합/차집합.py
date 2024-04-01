import sys

# 1822 차집합 실버4
input = sys.stdin.readline
n,m = map(int,input().split())
arr_n = list(map(int,input().split()))
arr_m = list(map(int,input().split()))
arr_n.sort()
arr_m.sort()
path = []

def binary_search(target):
    low = 0
    high = len(arr_m) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr_m[mid] == target:
            return True
        elif arr_m[mid] < target:
            low = mid + 1
        elif arr_m[mid] > target:
            high = mid -1
    return False

for i in arr_n:
    if not binary_search(i):
        path.append(i)

print(len(path))
if len(path) != 0 : print(*path)