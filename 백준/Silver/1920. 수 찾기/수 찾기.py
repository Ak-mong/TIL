# 수 찾기 실버 4 1920
def find_num(v):
    s = 0
    e = n
    if v < arr[s] or v > arr[e-1]:
        return 0
    while s <= e:
        half = (s + e) // 2
        if arr[half] == v:

            return 1
        elif arr[half] < v:
            s = half + 1
        else: # 탐색 중인 값이 찾는 값보다 클 때
            e = half -1
    return 0

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
find = list(map(int,input().split()))
for i in find:
    print(find_num(i))