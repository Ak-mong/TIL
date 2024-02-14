import sys;sys.stdin = open('txt/arr_sum.txt')

def dfs(n,k,s): # n 최종단계, k 현재단계, s 현재합
    global min_v
    if min_v < s: return  # 최소값이 더해져있는 s값보다 작을 경우 유망하지 않으므로 return
    # k 가 n의 수와 같아졌을 때
    if k == n:
        if min_v > s: # global의 min_v가 s보다 클 때
            min_v = s # 변경
            # print(p)
    else:
        for i in range(k,n): # 0 0 3
            p[k], p[i] = p[i], p[k]
            dfs(n,k+1,s+arr[k][p[k]])
            p[k], p[i] = p[i], p[k]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    # print(arr)
    min_v = 10*N
    dfs(N,0,0)
    print(f'#{tc} {min_v}')