import sys; sys.stdin = open('txt/binary.txt')


def countPage(page,goal):
    cnt = 0
    start = 1 #페이지 수는 양수기 때문에 1<= page<= 400 총 400장
    end = page # n-1을 쓰려면 인덱스 0부터 셈이 시작되야된다.
    while start <= end:
        mid = (start + end) // 2
        cnt += 1
        if mid == goal:
            return cnt
        elif mid > goal:
            end = mid
        else:
            start = mid
    return -1
t = int(input())
for tc in range(1,t+1):
    p, pa, pb = map(int,input().split())
    winner = ''
    #A가 이길경우
    if countPage(p,pa) < countPage(p,pb):
        winner = 'A'
    #b가 이길경우
    elif countPage(p,pa) > countPage(p,pb):
        winner = 'B'
    #비길경우
    else:
        winner = 0
    print(f'#{tc} {winner}')
