import datetime
# 실버 5

today = list(map(int,input().split()))
d_day = list(map(int,input().split()))

if d_day[0]-today[0] >1000:
    print('gg')
    exit(0)
elif d_day[0]-today[0] == 1000 and (today[1], today[2]) <= (d_day[1],d_day[2]):
    print('gg')
    exit(0)
else:
    todays = datetime.date(*today)
    d_days = datetime.date(*d_day)
    print(f'D-{d_days.toordinal()-todays.toordinal()}')