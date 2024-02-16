import sys; sys.stdin = open('../txt/tournament_card.txt')
def win(r1,r2):
    if arr[r1] == arr[r2]:
        return r1
    else:
        if arr[r1] ==1 and arr[r2] == 2: #가위 vs 바위
            return r2
        elif arr[r1] ==1 and arr[r2] == 3: #가위 vs 보
            return r1
        elif arr[r1] ==2 and arr[r2] == 1: #바위 vs 가위
            return r1
        elif arr[r1] ==2 and arr[r2] == 3: #바위 vs 보
            return r2
        elif arr[r1] ==3 and arr[r2] == 1: #보 vs 가위
            return r2
        elif arr[r1] ==3 and arr[r2] == 2: #보 vs 바위
            return r1

def game(i,j):
    if i ==j:
        return i
    else:
        r1 = game(i,(i+j)//2)
        r2 = game((i+j)//2+1,j)
        return win(r1,r2)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {game(0,N-1)+1}')