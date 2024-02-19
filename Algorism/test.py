import sys; sys.stdin = open('input.txt')
import math
import time
# N = int(input())
# # arr = list(map(int,input().split()))
# arr = [input() for _ in range(N)]
# arr = list(set(arr))
# arr.sort()
# # arr.sort()
# # print(arr)
# # arr_len = []
# for i in range(len(arr)):
#     # arr_len.append(len(i))
#     for j in range(len(arr)-i-1):
#         if len(arr[j])>len(arr[j+1]):
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# # for x in range(len(arr)-1):
# #     if len(arr[x]) == len(arr[x+1]):
# #         # 사전순 정렬
# #         for k in range(len(arr[x])):
# #             if ord(arr[x][k]) > ord(arr[x+1][k]):
# #                 arr[x],arr[x+1] = arr[x+1],arr[x]
# for i in arr:
#     print(i)
# # print(arr)
N = int(input())
arr = [input() for _ in range(N)]
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if len(arr[j]) > len(arr[j+1]):
#             arr[j],arr[j+1] = arr[j+1],arr[j]

for x in arr: print(x)
