import sys; sys.stdin = open('txt/stack1.txt')
t = int(input())
for tc in range(1,t+1):
    n = input()
    stack = []
    flag = 1
    top = -1
    for i in n:
        if top < -1:
            flag = 0
            break
        if i == '(':
            stack.append(i)
            top += 1
        elif i ==')':
            if top == -1:
                flag =0
                break
            stack.pop()
            top -= 1
    if stack:
        flag = 0

    print(f'#{tc} {flag}')

