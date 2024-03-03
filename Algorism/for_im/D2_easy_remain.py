import sys;sys.stdin=open('easy_remain.txt')

'''
각 동전간 배수 관계 +> 그리디 가능

'''
arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t= int(input())
for tc in range(1,t+1):
    n = int(input())
    cnt = [0] * 8
    # i = 0
    # while n >0 or i <= 7:
    #     if n >= arr[i]:
    #         n -= arr[i]
    #         cnt[i] += 1
    #     else:
    #         i += 1
    for i in range(8):
        if n // arr[i] >0:
            cnt[i] += n // arr[i]
            n = n % arr[i]
    print(f'#{tc}')
    print(*cnt)
