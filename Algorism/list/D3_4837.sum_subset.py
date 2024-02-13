import sys; sys.stdin = open('txt/sum_subset.txt','r')

arr = list(range(1, 13)) # 1~12
n = len(arr) # 12
t = int(input())
for tc in range(1,t+1):
    N, K = map(int,input().split())
    ans = 0
    for i in range(1,1<<n): # 1 이상 2의 12승 이하
        sums, cnt = 0,0
        for j in range(n): # 0부터 시작해야하지만 arr은 1부터 시작하기 때문 => 횟수만 가져오겠다.
            if i & 1<<j: # 1<<0 1<<1 1<<2 ... 랑 계속 비교해 간다
                sums += arr[j]
                cnt += 1
        if sums == K and cnt==N: # j 문이 돌고나서 부분집합의 합이 k와 같고, 부분집합의 원소의 갯수가 N과 같은지 확인
            ans += 1
    print(f'#{tc} {ans}')




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