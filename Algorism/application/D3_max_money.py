import sys;sys.stdin =open('txt/max_money.txt')
'''
첫번째 인덱스를 가지고 나머지 숫자 중 가장 큰 것과 바꾸기
두번째 인덱스를 가지고 나머지 숫자 중 가장 큰 것과 바꾸기
'''
def changeindex(x):

    if ''.join(n) in path:  # 가지치기
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
            changeindex(x+1)
            # path.pop()
            # n[i],n[x] = n[x],n[i] # 바꾸기
            n[i],n[j] = n[j],n[i] # 바꾸기

t = int(input())
for tc in range(1,t+1):
    n_,m = map(int,input().rsplit()) # 숫자, 횟수
    n = list(str(n_))
    len_n = len(n)
    path = []
    # print(len_n)
    # print(arr,m)
    cnt = 0
    changeindex(0)
    # print(*n)
    # print(path)
    if path:
        print(max(path))
    else:
        print(''.join(n))
    # print(cnt)
