import sys;sys.stdin=open('base_station.txt')

'''
h : 집들
a : 1 기지국
b : 2 기지국
c : 3 기지국
x : 없음
'''
drc = [[0,1],[1,0],[0,-1],[-1,0]]
def covering(r,c,length):
    for k in range(4):
        for len in range(1,length+1): # lebgtg 칸까지 가야되서
            nr = r + drc[k][0] * len
            nc = c + drc[k][1] * len
            if 0<= nr < n and 0<= nc < n and arr[nr][nc] == 'H':
                arr[nr][nc] = 'E'
t= int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
                if arr[i][j] == 'A':
                    covering(i,j,1)
                if arr[i][j] == 'B':
                    covering(i,j,2)
                if arr[i][j] == 'C':
                    covering(i,j,3)
    cnt = 0
    for p in range(n):
        for q in range(n):
            if arr[p][q] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')
    for x in arr:
        print(x)





