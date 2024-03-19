import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()

friends = ['a','b','c','d','e']
m = 5 # 친구의 수
n = 3

# 반복문 방법
for a in range(5):
	start1 = a+1
	for b in range(start1,5):
		start2 = b + 1
		for c in range(start2,5):
			print(friends[a], friends[b], friends[c])

# 재귀 방법
path = []
# 5C2
def getFriend(lev, start):
    if lev ==n:
        print(path)
        return

    for i in range(start,5):
        if used[i]: continue
        used[i] = 1
        path.append(friends[i])
        getFriend(lev + 1, i+1)
        path.pop()
        used[i] = 0

used = [0] * len(friends)
getFriend(0,0)