# 브론즈 1

arr = list(map(int,input().split()))
''' 
수를 상정하고 하나씩 더해가면서
5개의 수를 계속 나눠 보면서 count 해서 3개 이상일 경우
'''
n = 1
while True:
    cnt = 0
    for i in arr:
        if n % i ==0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1