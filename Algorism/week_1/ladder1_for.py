import sys;
sys.stdin = open('txt/ladder1.txt')
# sys.stdin = open('txt/ladder1_output.txt','w')
db = [0, 0, -1]
dp = [-1, 1, 0]
n = 100
def find_position(arr):
    for x in range(n):
        if arr[n-1][x] == 2:
            r = n-1
            c = x
            return r,c
def laddering(arr,r,c):
    for i in range(r,-1,-1):
        for j in range(n):
            if arr[i][j] == 1:
                if i == 0:
                    return i,j
                for k in range(3):
                    nb = i + db[k]
                    np = j + dp[k]
                    if 0<= nb < n and 0<= np < n and arr[nb][np] == 1:
                        i,j = nb,np
                        arr[i][j] = 9
            # elif i == 0 and j == c:
            #     return j
            else:
                continue
    return -1
t = 10
for tc in range(1, t+1):
    num = int(input())
    ladder_list = [list(map(int,input().split())) for _ in range(n)]
    r,c = find_position(ladder_list)
    print(laddering(ladder_list,r,c))

    # print(f'#{tc} {ladder_list}')