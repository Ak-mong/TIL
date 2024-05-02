import sys
input = sys.stdin.readline

# 26099 설탕 배달 2 실버4
sugar = int(input())
cnt = 0
while sugar >=0:
    if sugar %5 == 0:
        cnt += sugar//5
        break
    sugar -= 3
    cnt += 1
if sugar <0:
    print(-1)
else:
    print(cnt)