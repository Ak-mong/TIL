import sys;sys.stdin =open('txt/tournament_card.txt')
def divided_person(i,j): # i번부터 j번까지 속한 그룹을 나눠버린다
    a = len(list(range((i+j)//2+1))) # 0 ~ (i+j) // 2
    b = len(list(range((i+j)//2+1, N))) # (i+j) //2 +1 ~ N
    return a,b

def rsp() : #rock scissors paper

def divide_two(start, end):
    if start == end:
        return start  # 한명 남았다는 의미이므로 가위바위보를 위해 리턴

    a = divide_two(start, (start + end) // 2)
    b = divide_two((start + end) // 2 + 1, end)
    return rsp(a, b)  # 가위바위보 실시


def rsp(x, y):
    if arr[x] == arr[y]:  # 비긴 경우
        return x
    elif arr[x] - arr[y] == 1 or arr[x] - arr[y] == -2:  # x가 이긴 경우
        return x
    return y


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(f'#{tc+1} {divide_two(0, N-1)+1}')