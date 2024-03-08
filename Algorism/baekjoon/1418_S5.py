import sys;sys.stdin=open('input.txt')

n = int(input())
k = int(input())
result = 0

# 소수찾기
prime_num = [1] * (n*1)
for i in range(2,int(n**0.5)+1):
    if prime_num[i]:
        for j in range(2*i,n,i):
            prime_num[j] = 0
print(prime_num)





























# while i**2 <= n:
# primeList = [1] * (n+1)
# for i in range(2,int(n**(0.5))+1):
#     if primeList[i]:
#         for j in range(2*i,n+1,i):
#             primeList[j] = 0
# # 소수 판별
# print(primeList)
# k_number = [1] * (n+1)
# for i in range(2,n+1):
#     if primeList[i] and i > k:
#         for j in range(i,n+1,i):
#             k_number[j] = 0
# print(k_number)
# print(sum(k_number)-1)

# for i in range(1,n+1):
#     arr = []
#     flag = 1
#     # j = 2
#     cnt = 0
#     for j in range(2,int(i**(0.5))+1):
#     # while j*j <= i:
#         while i % j ==0 and j <= k:
#             flag = 0
#             # arr.append(j)
#             i //= j
#         j += 1
#     if flag:
#         arr.append(i)
#     # if j < i and i <= k:
#     #     arr.append(i)
#         # cnt += 1
#     print(arr)
#     # if cnt > 0:
#     #     result += 1
# print(result)