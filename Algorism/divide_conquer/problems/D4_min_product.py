import sys; sys.stdin = open('min_product.txt')

'''
가로 세로 겹치지 않는 칸을 더한 값의 최소 값
'''
# 순열 구하기
def perm(level,cursum):
    global min_v, cnt
    if min_v < cursum: return
    # cnt += 1
    if level == n:
        # 원하는 행동
        if min_v > cursum:
            min_v = cursum
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        path.append(arr[level][i])
        perm(level+1, cursum + arr[level][i])
        path.pop()
        used[i] = 0
t = int(input())
for tc in range(1,t+1):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]
    # print(arr)
    path = []
    used = [0] * n
    min_v = 111111111111111111111111
    cnt = 0
    perm(0,0)
    print(f'#{tc} {min_v}')
    # print(cnt)




















'''
# 순열
def perm(level,cursum):
    global result
    if cursum > result: return
    if level == n:
        # print(path)
        if cursum < result:
            result = cursum
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        # path.append(arr[level][i])
        perm(level+1, cursum+arr[level][i])
        # path.pop()
        used[i] = 0




t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # for i in arr:
    #     print(i)
    path = []
    result = 10000000000000000000
    used = [0] * n
    perm(0,0)
    # for i in range(len(arr)):
    # print()
    print(f'#{tc} {result}')
'''