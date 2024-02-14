import sys;sys.stdin =open('txt/tournament_card.txt')
def divided_person(i,j): # i번부터 j번까지 속한 그룹을 나눠버린다
    if i == j: return i # 한명 남았다 => 모든 가위바위보가 완료됐다.
    a = divided_person(i,(i+j)//2) # a그룹
    b = divided_person((i+j)//2+1,j) # b그룹
    return rsp(a,b) # a,b 중에 이긴 승자가 리턴된다.

def rsp(a,b): # 두 그룹간 가위바위보
    if arr[a] == arr[b]: # 비길 때 a가 우선시 됨
        return a
    if arr[a]-arr[b] == 1 or arr[a] - arr[b] == -2:
        return a # a가 이기는 상황
    return b # a가 이길 상황이 안나왔기 때문

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split())) # 인덱스 개수를 맞추기 위해 [0] 을 추가했음
    print(f'#{tc} {divided_person(1,N)}')