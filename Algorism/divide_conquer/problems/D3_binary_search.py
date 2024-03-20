import sys; sys.stdin=open('binary_search.txt')

def binary_search(target):
    global cnt
    left = 0
    right = len(arr_a) - 1
    flag = -1
    while left <= right:
        mid = (right + left) // 2
        if target == arr_a[mid]:
            cnt += 1
            return
        elif target < arr_a[mid]:
            if flag == 0: # 왼쪽일 때 0으로 취급
                break
            flag = 0
            right = mid - 1
        elif target > arr_a[mid]:
            if flag == 1:
                break
            flag = 1
            left = mid + 1
    return -1




t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr_a = list(map(int,input().split()))
    arr_a.sort()
    arr_b = list(map(int,input().split()))
    cnt = 0
    for i in arr_b:
        binary_search(i)
    print(f'#{tc} {cnt}')




# def binary_search(x): # x 찾아야 할 수
#     global cnt
#     l = 0
#     r = len(arr_a)-1
#     flag = -1
#     while l <= r:
#         mid = (l + r) // 2
#         if arr_a[mid] == x:
#             cnt += 1
#             return
#         elif arr_a[mid] > x:
#             if flag ==0:
#                 break
#             r = mid - 1
#             flag = 0
#         elif arr_a[mid] < x:
#             if flag == 1:
#                 break
#             l = mid + 1
#             flag = 1
#     return -1








