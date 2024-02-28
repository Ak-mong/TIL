import sys;sys.stdin =open('txt/max_money.txt')
'''
첫번째 인덱스를 가지고 나머지 숫자 중 가장 큰 것과 바꾸기
두번째 인덱스를 가지고 나머지 숫자 중 가장 큰 것과 바꾸기
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
'''
def changeindex(x,depth):

    # if ''.join(n) in path:  # 가지치기
    #     return
    # 가지치기,
    if ''.join(n[:]) in path[depth]:
        return
    if x == m: # 횟수만큼만 반복
        path.append(''.join(n[:]))
        # print(path)
        return

    # for i in range(len_n - 1, x - 1, -1):  # x에서 n까지 비교하면서 반복
    #     if n[x] < n[i]:
    for i in range(len_n-1): # x에서 n까지 비교하면서 반복
        for j in range(i+1,len_n):
            # n[i],n[x] = n[x],n[i] # 바꾸기
            n[i],n[j] = n[j],n[i] # 바꾸기
            # path.append(''.join(n[:]))
            # cnt += 1
            changeindex(x+1,depth+1)
            # path.pop()
            # n[i],n[x] = n[x],n[i] # 바꾸기
            n[i],n[j] = n[j],n[i] # 바꾸기

t = int(input())
for tc in range(1,t+1):
    n_,m = map(int,input().rsplit()) # 숫자, 횟수
    n = list(str(n_))
    len_n = len(n)
    path = [[] for _ in range(m+1)]
    # print(len_n)
    # print(arr,m)
    cnt = 0
    changeindex(0,0)
    # print(*n)
    # print(path)

    # if path:
    #     print(max(path[m]))
    # else:
    #     print(''.join(n))
    # print(cnt)
