import sys; sys.stdin = open('txt/electric_bus')
"""
정류장 0 ~ n+1
한번 충전으로 최대 k감
충전기 설치 m개의 정류장
최소 몇번으로 종점 도착
종점에 도착x == 0

"""

t = int(input())
for tc in range(1,t+1):
    k,n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    x = 0
    cnt = 0
    arr = [0]+ arr + [n] # 마지막 n(종점)과 시작점(0)의 위치를 기록

    for i in range(len(arr)):
        # 버스가 앞으로 못갈 때
        if arr[i] - arr[i-1] > k:
            cnt = 0
            break
        # 버스가 앞으로 갈 수 있는데, k 만큼 이동 한 현재 위치가 충전기가 있는 정류장 보다 작을 때, 그 이전 충전기 위치로 간다
        elif x + k < arr[i]:
            x = arr[i-1]
            cnt += 1
    print(f'#{tc} {cnt}')