import sys;sys.stdin=open('input.txt')
# 22378 영화 평가 브론즈1
'''
중위평균구하는거
'''
n, l, h = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
# print(arr)
sum_v = 0
for i in range(l,n-h):
    sum_v += arr[i]
average_v = sum_v / (n-(l+h))
print(average_v)
