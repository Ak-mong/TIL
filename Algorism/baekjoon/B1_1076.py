import sys;sys.stdin= open('input.txt')
import time
starttime= time.time()
# 암호키 브론즈1
# def find(arr):
#     for i in range(len(arr)):
#         if arr[i] < 10**6:
#             return 'NO'
#     return 'YES'
n = int(input())
for tc in range(n):
    s = int(input())
    for i in range(2,10**6 +1):
        if s%i ==0:
            print('NO')
            break
        elif i == 10**6:
            print('YES')

    # print(prime_list)

# print(time.time()-starttime)