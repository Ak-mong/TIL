import sys;sys.stdin=open('electric_bus.txt')

def dfs(level,e,cnt):
    global ans
    # 가지치기
    if ans < cnt: return
    # 기저조건
    if level == n:
        ans = min(ans,cnt)
        return
    dfs(level+1,arr[level]-1,cnt + 1) # 충전 함
    if e > 0: # 충전량이 없으면 그 다음 정류장으로 못감
        dfs(level+1,e-1,cnt) # 충전 안 함

t = int(input())
for tc in range(1,t+1):
    arr = list( map(int,input().split()))
    ans = 987654321
    n = arr[0]
    dfs(2,arr[1]-1,0) # 2번 정류장일 때 1번정류장에서 충전
    print(f'#{tc} {ans}')
