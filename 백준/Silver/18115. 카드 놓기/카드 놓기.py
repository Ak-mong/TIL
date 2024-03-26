# 18115 카드 놓기 실버3
from collections import deque
n = int(input())
skill = list(map(int,input().split()))
skill.reverse()
new_arr = deque()
for i in range(1,n+1):
    if skill[i-1] ==1:
        new_arr.appendleft(i)
    elif skill[i-1] ==2:
        new_arr.insert(1,i)
    elif skill[i-1] ==3:
        new_arr.append(i)
print(*new_arr)