import sys; sys.stdin = open('txt/sum_subset.txt','r')

t = int(input())
for tc in range(1,t+1):
    n, k = list(map(int,input().split()))
    cnt = 0

    for i in range(1,1<<n):
        sums = 0
        for j in range(n):
            sums += i + j
            # print('i j ',i,j)
        # print(i,j,sums)
        if sums == k:
            cnt +=1
        # print()
    print(f'#{tc} {cnt}')




# sum = 0
# a = []
# T = int(input())
# for i in range(1, 13):
#     a.append(i)
# print(a)
# for t in range(T):
#     result = 0
#     N, K = map(int, input().split())
#     A = a + [0] * N
#     print(A)
#     for k in range(13):
#         for j in range(N):
#             sum = sum + A[k + j]
#         if K == sum:
#             result += 1
#         sum = 0
#     print(f'#{t + 1} {result}')