import sys;sys.stdin = open('input.txt')
# 새로운 달력 실버 5 12437
'''
새로운 달력을 만들자
첫달의 첫날은 첫번째 열에 위치
첫달을 제외한 각 달의 첫날은 이전달의 마지막 날 다음 열
달력은 1년치
한달에 11일 1년에 3달 한주에 4일이라면?

년당월 월당일 주당일 
    3   11      4
'''
t = int(input())
for case in range(1,t+1):
    year_month, month_day, week_day = map(int,input().split())
    # for i in range()
    line = 1
    col = 1
    cnt = 1
    while cnt < year_month * month_day:

        if col == week_day and cnt % month_day == 0:
            col = 1
            line += 1
            cnt += 1
        elif col == week_day:
            col//=week_day
            line += 1
            cnt += 1
        elif cnt % month_day == 0:
            line += 1
            col += 1
            cnt += 1
        else:
            col += 1
            cnt += 1

    print(f'Case #{case}: {line}')