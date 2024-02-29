import sys;sys.stdin= open('txt/max_money.txt')
'''
조합 문제
level = 10
branch = 6C2 = 15 

'''
def get_len(price):
    cnt = 0
    while price:
        price //= 10
        cnt += 1
    return cnt

def swap(price,i,j):
    # itoa
    price_arr = [0] * price_len
    for k in range(price_len-1,-1,-1):
        price_arr[k] = price % 10
        price //= 10
    # swap
    price_arr[i], price_arr[j] = price_arr[j],price_arr[i]

    #atoi
    price = 0
    for k in range(price_len):
        price = price * 10 + price_arr[k]
    return price

def find_max(n,k,price): # n 바꾸는 횟수 k 현재 레벨, price 숫자판(정수)
    global ans
    # 메모이제이션 + 가지치기
    # for i in range(MAXSIZE):
    #     if memo[k][i] == 0:
    #         memo[k][i] = price
    #         break
    #     elif memo[k][i] == price:
    #         return
    if ans > price: return
    if n == k:
        if ans < price:
            ans = price
        return
    #nC2
    for i in range(price_len-1):
        for j in range(i+1,price_len):
            find_max(n,k+1, swap(price,i,j))

MAXSIZE = 720 # 6!
t = int(input())
for tc in range(1,t+1):
    price, n = map(int,input().split())
    memo = [[0] * MAXSIZE for _ in range(n+1)]
    ans = 0
    # arr = list(map(int,input().split()))
    price_len = get_len(price)
    find_max(n,0,price)
    print(f'#{tc} {ans}')