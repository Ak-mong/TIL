import sys
input = sys.stdin.readline
#11699 구간 합 구하기 4 실버3
n,m = map(int,input().split())
arr = list(map(int,input().split()))
sum_arr = [0]*(n+1)

for x in range(1,n+1):
    sum_arr[x] = sum_arr[x-1] + arr[x-1]
# print(sum_arr)
for x in range(m):
    i,j = map(int,input().split())
    print(sum_arr[j]-sum_arr[i-1])