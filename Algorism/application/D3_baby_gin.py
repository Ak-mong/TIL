import sys;sys.stdin = open('txt/baby_gin.txt')

def baby_gin(arr):
    runs = 0
    triplet = 0
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]
    if arr1[0] == arr1[1] and arr1[1] == arr1[2]:
        runs += 1
    if arr2[0] == arr2[1] and arr2[1] == arr2[2]:
        runs += 1
    if arr1[0]+1 == arr1[1] and arr1[1]+1 == arr1[2]:
        triplet += 1
    if arr2[0]+1 == arr2[1] and arr2[1]+1 == arr2[2]:
        triplet += 1
    if runs + triplet == 2:
        return 1
    return 0
def makePerm(x):
    global flag
    if x == 6:
        if baby_gin(path): flag = 1
        # print(path, end=' ')
        return
    for i in range(6):
        if used[i]: continue
        used[i] = 1
        path.append(arr[i])
        # path.append(i)
        makePerm(x+1)
        path.pop()
        used[i] = 0

t = int(input())
for tc in range(1,t+1):
    arr = list(map(int,input()))
    # print()
    # print(f'#{tc}',arr)
    flag = 0
    # 6 장 중에 3장
    # level 3 branch 6
    path = []
    used = [0] * len(arr)
    makePerm(0)
    print(f'#{tc} {flag}')