import sys;sys.stdin = open('txt/min_sum.txt')
'''
최소합 구하기
모든 경로를 구해서 구하거나, 짧은 경로로만 구하던가
'''

def brute_force(y,x):
    global result, sum_v
    if result < sum_v: # result가 이미 작으면 굳이 실행안해도 된다.
        return
    if y == n-1 and x == n-1: # 마지막 좌표에 다달았을 때
        result = sum_v
        return
    for dy,dx in dij:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < n:
            sum_v += arr[ny][nx] # 탐색 전 더해보기
            brute_force(ny,nx) # 새 좌표로 탐색하기
            sum_v -= arr[ny][nx] # 탐색 끝났으니 빼기

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # print('#',tc)
    # for x in arr:
    #     print(x)
    
    dij = [[0, 1], [1, 0]]  # 오 아
    sum_v = arr[0][0] # 시작점
    result = 100 # 최대한 큰 값으로
    brute_force(0,0) # 0,0 부터 시작하니까...
    print('#',tc,result)






