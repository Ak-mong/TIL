import sys;sys.stdin= open('high_self.txt')

'''
문제 키워드
- 선반 높이 B
- 키
=> B 보다 작아서, 탑을 쌓을거야
    -> 탑의 높이 : 점원들의 키(H)의 합
    
=> B 이상으로 탑을 쌓아라
= B 이상의 탑중 가장 작은 탑

1. 이분탐색
2. 완전탐색

경우의 수를 모두 보면 될까?
2. 알고리즘
    - DFS + 백트래킹
=> 시간복잡도 ? 
 20! 정도
 => 가지치기가 말이 되는것 같은데?
 단순한 BFS로 가능한가?
=> 똑같은 로직으로 다르게 구현할 수 있나?
    -> 자료구조를 바꿀수 있나?
    -> 접근법을 조금 바꿀 수 없나?
고를까 말까로 풀 수 없을까?
'''

def dfs(cnt,sum_height):
    global ans
    # 기저조건
    '''
    # 1. 모든 점원이 탑을 쌓았데 고려가 되었다면?
    -> 현재까지 쌓은 점원의 수
    # 2. 키의 합이 B 이상이면 종료
    -> 현재까지 쌓은 탑의 높이
    '''

    if sum_height >= b: # 2번 조건
        # 제일 높이가 낮은 탑이 정답
        # 최소 탑의 높이는 재귀호출함수들이 "동시에" 사용함 -> 전역변수로 사용
        ans = min(ans,sum_height)
        return
    
    if cnt == n: # 1번 조건이 뒤로 가야된다. 다 쌓았을 때를 고려못함
        return
    
    # 재귀호출 하트
    # 쌓는다 안쌓는다
    dfs(cnt + 1, sum_height + arr[cnt])
    dfs(cnt + 1, sum_height)

t = int(input())

for tc in range(1,t+1):
    n,b = map(int,input().split())
    arr = list(map(int,input().split()))
    # print(arr)
    ans = int(1e9)
    dfs(0,0)
    print(f'#{tc} {abs(ans - b)}')