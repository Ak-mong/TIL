import sys;sys.stdin = open('group_divide.txt')

def find(x):
    # 기저 조건

    # 재귀함수 호출 전

    # 재귀함수 호출
    for to in adj_lst[x]:


t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    adj_lst = {x:[] for x in range(1,n+1)}
    for i in range(0,m,2):
        adj_lst[arr[i]].append(arr[i+1])
    print(adj_lst)
    visited = [0] * n

    find(1)