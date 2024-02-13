import sys;
sys.stdin = open('txt/ladder1.txt')
# sys.stdin = open('txt/ladder1_output.txt','w')
db = [0, 0, -1]
dp = [-1, 1, 0]
n = 100
def find_position(arr):
    for x in range(n): # 당첨! 의 위치를 찾은 것
        if arr[n-1][x] == 2:
            r = n-1
            c = x
            return r,c
def laddering(arr,r,c):
    while True: # find_position()를 돌고 나온 r,c를 이용해 당첨자리에서 부터 위로 하나씩 올라가면서 비교
        if r == 0:
            return c
        for i in range(3): #3방향 탐색
            nb = r + db[i] # r -> 위
            np = c + dp[i] # c -> 왼, 오
            if 0<= nb < n and 0<= np < n and arr[nb][np] == 1:
                r,c = nb,np
                arr[nb][np] = 9
t = 10
for tc in range(1, t+1):
    num = int(input())
    ladder_list = [list(map(int,input().split())) for _ in range(n)]
    r,c = find_position(ladder_list)
    print(f'#{tc} {laddering(ladder_list,r,c)}') # 실수함!!!!
    # 함수에서 처리된 c를 넣어야 됬음, 그냥 c를 넣으면 find_posiont()이 돌아간 c가 나옴