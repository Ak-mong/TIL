import sys;
# 9012 괄호 실버4

t = int(sys.stdin.readline().strip())
for tc in range(t):
    arr = list(sys.stdin.readline().strip())
    stack = []
    flag = 'YES'
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                flag = 'NO'
                break
    if stack: flag = 'NO'
    print(flag)