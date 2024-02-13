import sys;sys.stdin = open('txt/find_road.txt')
A =0
B =99
node = 98 # A,B를 제외한 정점의 개수
for _ in range(10):
    T, N = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [0] * 100
    # print(T,N)
    stack = []
    n1, n2 = [0]*100, [0]*100
    for i in range(1,node+1):
        visited[0] = 1
        if visited[i] ==0:
            n1[i] = i
            stack.append(i)
        elif visited[i] == 1:
            n2[i] = i
            stack.append(i)
        # if visited[i] == 1 and n2[i] == i: # 두 번 다 갔을 경우

