import sys
from collections import deque
sys.stdin =open('input.txt')
# input = sys.stdin.readline()
from collections import deque
n = int(input())
arr = deque(map(int,input().split()))

# arr.reverse()
print(arr)
new_arr = deque()

for i in range(1,n+1):
    method = arr.pop()
    if method == 1:
        new_arr.appendleft(i)
    elif method == 2:
        new_arr.insert(1,i)
    else:
        new_arr.append(i)
print(new_arr)

