import sys
input = sys.stdin.readline
# 2716 원숭이 매달기 실버2
n = int(input())
for i in range(n):
    strings = input().strip()
    tree = []
    max_depth = 0
    for x in strings:
        if x == '[':
            tree.append(x)
        else:
            max_depth = max(max_depth, len(tree))
            tree.pop()
    print(2 ** max_depth)