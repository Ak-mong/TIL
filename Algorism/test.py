import sys;sys.stdin =open('input.txt')

# def changeindex(level, depth):
#     if level == n:
#         path.append(arr[:])
#         return
#     for i in range(n-1):
#         for j in range(i+1,n):
#             arr[i],arr[j] = arr[j], arr[i] # 바꾸고
#             changeindex(level+1,depth+1)
#             arr[i],arr[j] = arr[j], arr[i] #다시 되돌리기
#
# t = int(input())
# for tc in range(1,t+1):
#     arr_,count_ = map(str,input().split())
#     count = int(count_)
#     arr = list(arr_)
#     n = len(arr)
#     # print(arr)
#     path = [[] * n for _ in range(n)]
#     # path = []
#     path2 = []
#     changeindex(0,0)
#     print(path2)

'''
for i 720 <- 6!
    if m[k][i] == 0:
        m[k][i] ==price
        break
    elif m[k][i] == price
        return # 가지치기
'''
#
# money = [5, 20, 100]
# money.sort(reverse=True)
# min_cnt = 10
# n = len(money)
# def moneymoney(sum,cnt):
#     global min_cnt
#     if min_cnt < cnt:
#         return
#     if sum == 0:
#         if min_cnt > cnt:
#             min_cnt = cnt
#         return
#     for x in range(n):
#         moneymoney(sum-money[x],cnt +1)
#
# moneymoney(530,0)
# print(min_cnt)
#
def find(sugar,cnt):
    global min_cnt, flag
    if sugar < 0:
        # flag = 0
        return
    if min_cnt < cnt:
        return
    if sugar == 0:
        flag = 1
        if min_cnt > cnt:
            min_cnt = cnt
        return
    for x in range(2):
        find(sugar - arr[x],cnt +1)
    if min_cnt == 10000000000:
        flag = 0
        return
t = int(input())
for tc in range(t):
    arr = [5,3]
    n = int(sys.stdin.readline())
    min_cnt =10000000000
    flag = 1

    find(n,0)
    if flag:
        print(min_cnt)
    else:
        print(-1)