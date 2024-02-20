import sys;sys.stdin =open('input.txt')
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로 단어 정렬
# 중복된 단어는 하나만 남기고 제거
# lambda 이용
# N = int(sys.stdin.readline().rstrip())
# def MenOfPassion(n):
#     global cnt
#     sum = 0
#     for i in range(1,n-1):
#         for j in range(i+1,n):
#             for k in range(j+1, n+1):
#                 # sum = sum + arr[i] * arr[j] * arr[k] # 코드1
#                 sum = sum + 1 * 2 * 3 # 코드1
#                 cnt += 1
#     return cnt
# cnt = 0
# arr = [0] * N
# print(MenOfPassion(N))
# print(3)
n = int(input())
cnt = n-2
sum = 0
for i in range(1,n-1):
    sum += cnt*i
    cnt -= 1
print(sum)
print(3)