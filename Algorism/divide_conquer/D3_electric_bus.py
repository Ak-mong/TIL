import sys;sys.stdin=open('electric_bus.txt')
'''
최소한의 교체 횟수로 목적지 도착
출발지는 교환횟수에서 제외
충전이 아닌 교체
1 2 3 4 5
2 3 1 1 0
1-2,2-5 한번교체가 답
배터리 하나로 가는 횟수 -1 = 교체 횟수
배터리 용량만큼 가는데 중간에 현재 배터리 용량보다 큰게 있다면 멈추고 거기서 부터 시작
'''
def bus(start):
    global length, cnt
    if length < len(path): return
    cnt += 1
    if start < n:
        value = arr[start]
        if value == 0:
            if length > len(path):
                length = len(path)
            # print(length)
            return length
        for i in range(value,0,-1): # 역순으로 갈 수 있을 만큼
            path.append(arr[start])
            bus(start + i)
            path.pop()

        return length-1

def buss(arr):
    i = 0
    while i <= n-1:
        for j in range(arr[i]):
            if arr[i] < arr[j]:
                pass

t = int(input())
for tc in range(1,t+1):
    arr = list(map(int,input().split()))
    n = arr[0]
    arr = arr[1:] + [0]
    temp = [0] * n
    path = []
    # print(bus(arr))
    # print(n,arr)
    cnt = 0
    length = 1000000000000000
    # buss(arr)
    print(f'#{tc} {bus(0)}')
    # print(cnt)

# def bus(arr):
#     cnt = 0
#     i = 0
#     while i < n:
#         j = arr[i]
#         for k in range(i+1,i+j+1):
#             if k == n-1:
#                 return cnt
#             if arr[k] > arr[i]:
#                 i = k
#                 break
#             else:
#                 i += 1
#             if i ==n:
#                 break
#         cnt += 1
#
#     return cnt