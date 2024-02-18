import sys; sys.stdin = open('input.txt')
import time
# N = input()
N = int(input())
N_ = N
new_num = 0
cnt = 0 #사이클 횟수
# while int(N) != new_num:
#     new_num = 0
#     if int(N) < 10:
#         N = '0' + N
#     for i in N:
#         new_num += int(i)
#     N = str(int(N[-1]) + new_num%10)
#     cnt+= 1
# print(cnt)
while True:
    new_num = 0
    for i in str(N_):
        new_num += int(i)
    N_ = int(str(N_%10) + str(new_num%10))
    # print(N_)
    cnt += 1
    if N_ == N:
        break
print(cnt)