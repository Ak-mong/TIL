import sys;sys.stdin=open('base_station.txt')

'''
h : 집들
a : 1 기지국
b : 2 기지국
c : 3 기지국
x : 없음
'''
dij = [[0,1],[1,0],[0,-1],[-1,0]]
t= int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    for x in arr:
        print(x)
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if arr[i][j] == 'A':
                    ni = i + dij[k][0]
                    nj = j + dij[k][1]




