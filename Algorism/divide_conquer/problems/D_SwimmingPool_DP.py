import sys;sys.stdin = open('swimmingpoll.txt')

'''
# 이 문제가 왜 DP로도 해결이 가능할까?

1. 작은 문제로 분할 할 수 있어야 한다.
    - 전체의 합 = 각 달까지의 최소들이 쌓여서 완성
    - 각 달까지의 최소 비용 문제로 분할
2. 뒤의 결과를 구할 때, 앞의 결과가 바뀌면 안된다.
'''


t = int(input())
for tc in range(1,t+1):
    cost = list(map(int,input().split()))
    # 1부터 쓰고싶어 == 맨 앞에 0 넣어두기
    days = [0] + list(map(int,input().split()))
    # DP 배열
    plans = [0] * 13 # 각 달까지의 최소금액을 저장

    # 1~ 12월
    for i in range(1,13):
        # 현재 달의 최소 비용 계산
        # 이전 달 + 1일권 구입 / 이전 달 + 1달권 구입 / 3달 전 + 3달권 구입, 그 중에서 최소
        plans[i] = min(plans[i-1] + (days[i] * cost[0]), plans[i-1] + cost[1])

        if i >= 3:
            plans[i] = min(plans[i], plans[i-3] + cost[2])
    #12월까지의 계산 결과 or 1년권
    min_cost = min(plans[12], cost[3])
    print(f'#{tc} {min_cost}')
