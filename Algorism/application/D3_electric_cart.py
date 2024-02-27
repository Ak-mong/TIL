import sys;sys.stdin = open('txt/electric_cart.txt')
t = int(input())
'''
가는길과 오느길의 전력 소비가 다름
123 -> 1 2 3 1 / 1 3 2 1 로 돌아올 수 있음
최소 소비량 구하기 
'''
def electric(idx,s,k): # 방문한 곳 수, 에너지 합, 현재위치
    global min_sum,cnt
    if idx == n: # 모두 방문했을 때
        s += arr[k][0]# 무조건 사무실로 돌아옴
        if min_sum > s: min_sum = s # 기존의 min_sum이 현재 s 보다 크다면? 값을 바꿔라
        return
    if s > min_sum: # s 가 min_sum 보다 크다면 가지치기
        return
    for i in range(1,n):
        if visited[i]: continue
        # if visited[i] ==0:
        visited[i] = 1 # 방문체크
        # result.append(arr[y][i])
        cnt += 1
        electric(idx+1,s+arr[k][i],i)
        # result.pop()
        visited[i] = 0 # 방문체크 해제



for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0] * (n+1)
    visited[0] = 1 # 시작점 방문체크
    min_sum = 1010000000000
    cnt = 0
    electric(1,0,0)
    print(f'#{tc} {min_sum}')