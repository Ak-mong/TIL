# 9934 완전 이진 트리 실버1
# 전위순회? 왼 나 오
def front(v):
    if v < 2**k:
        global value
        front(v*2)
        visited[v] = (arr[value])
        # print(v)
        value += 1
        front(v*2+1)

k = int(input())
arr = list(map(int,input().split()))
visited = [(0,) * 2 for _ in range(2**k)]
value = 0
front(1)
i = 1
while i < 2**k:
    for j in range(i):
        print(visited[i+j], end=' ')
    print()
    i *= 2