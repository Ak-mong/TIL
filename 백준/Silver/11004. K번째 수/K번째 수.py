import sys
input = sys.stdin.readline
# 11004 k번째 수 실버5
n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
print(arr[k-1])