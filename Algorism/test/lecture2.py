import sys; sys.stdin = open('algo2_sample_in.txt')
'''
행렬탐색
최대값의 합 구하기
m*m 최대값 찾고 그걸 시작점으로 또 탐색

벽체크 해야됨'''
def find_max(r,c):
    global max_v
    
    # 벽체크
    r_,c_ = r,c
    for i in range(m):
        for j in range(m):
            if r+i<n and c+j < n:
                if max_v < arr[r+i][c+j]:
                    max_v = arr[r+i][c+j]
                    r_,c_ = r+i,c+j
    r,c = r_,c_
    if sum_arr and sum_arr[-1] == arr[r_][c_]:
        return
    sum_arr.append(arr[r][c])
    find_max(r, c)


t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_v = 0
    sum_arr = []
    find_max(0,0)
    print(f'#{tc} {sum(sum_arr)}')
    # print()

sr,sc = 0,0
flag = 1
result = 0
while flag:
    max_r,max_c = sr,sc
    for i in range(sr,sr+m):
        for j in range(sc,sc+m):
            if 0<= i < n and 0 <= j < n and arr[i][j] > arr[max_r][max_c]:
                max_r = i
                max_c = j
    if max_r == sr and max_c == sc:
        if sc != 0 and sr != 0:
            flag = 0
            break
    else: 
        result += arr[max_r][max_c]
        sc = max_c
        sr = max_r
