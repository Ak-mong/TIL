import sys
input = sys.stdin.readline
# 28278 스택 2 실버4
n = int(input())
stack = []
for i in range(n):
    value = list(map(int,input().split()))
    if value[0] == 1:
        if len(value) == 2:
            stack.append(value[1])
    elif value[0] == 2:
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif value[0] == 3:
        print(len(stack))
    elif value[0] == 4:
        print(0 if stack else 1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)