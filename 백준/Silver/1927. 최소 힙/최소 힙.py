import sys
# 최소 힙
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    if a == 0:
        if not arr:
            print(0)
            continue
        else:
            s = heapq.heappop(arr)
            print(s)
    elif a > 0:
        heapq.heappush(arr,a)