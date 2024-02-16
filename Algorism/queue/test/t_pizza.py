import sys; sys.stdin = open('../txt/pizza.txt')

def solve(arr):
    Q = list(range(1,N+1)) # Q = [i for i in range(1,N=1)

    idx =N +1 # 다음에 화덕에 들어갈 피자 번호
    while len(Q) >1:
        # 피자를 꺼내서 치즈 확인
        p = Q.pop(0)
        arr[p] = arr[p] //2
        # 치즈가 남아 있으면 ==> 다시 넣기
        if arr[p] != 0:
            Q.append(p)
        # 치즈가 다 녹았으면 ==> 다음 피자 넣기
        elif idx <= M:
            Q.append(idx)
            idx += 1
    return  Q[0]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [0] + list(map(int,input().split()))
    arr_ = [(i,arr[i]) for i in range(M)]
    print(solve(arr))