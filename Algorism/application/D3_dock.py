import sys;sys.stdin=open('txt/dock.txt')

'''
0~0시 까지 24시간
A 도크의 사용신청 확인
최대한 많은 화물차 +> 최대 몇개
매시 정각으로 표시됨
앞 작업 종료와 동시에 다음 작업 시작
~5시 와 5시~  가능
'''
def docker(s):
    for i in range(n): # 10개의 스케쥴 중
        arr[i][0]
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr= [list(map(int,input().split())) for _ in range(n)] # s 시작 e 종료
    arr.sort(key=lambda x:x[1]) # 종료시간을 기준으로 정렬
    s = 0
    i = 0
    cnt = 0
    while s<=24:
        if i ==n:
            break
        if s <= arr[i][0]:
            s = arr[i][1]
            cnt += 1
        i += 1
    print(f'#{tc} {cnt}')