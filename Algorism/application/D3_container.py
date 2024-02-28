import sys;sys.stdin= open('txt/container.txt')

'''
n 개의 컨테이너를 m대의 트럭으로 A to B
트럭당 한개의 컨테이너
컨테이너 무게 <= 트럭 적재용량 
총 중량이 최대가 되자
트럭이나 화물은 남을 수 있음
컨테이너를 하나도 못옮기면 0 
'''
t = int(input())
for tc in range(1,t+1):
    # print('#',tc)
    n,m = map(int,input().split())# 컨테이너 수 , 트럭 수
    w = list(map(int,input().split()))# 컨테이너 당 무게
    t = list(map(int,input().split()))# 트럭당 무게
    ok = []
    w.sort(reverse=True)
    t.sort(reverse=True)
    # print(w)
    # print(t)

    # print(w,t)
    if len(t) >= len(w):
        length = len(w)
    else:
        length = len(t)
    i,j = 0,0
    while i < len(w) and j < len(t): # 둘 중 하나가 끝까지 들어갔을 때
        if w[i] <= t[j]:
            ok.append(w[i])
            j += 1
            i += 1
        else:
            i += 1
    # print(ok)
    print(f'#{tc} {sum(ok)}')

