import sys; sys.stdin = open('txt/forth.txt')

T = int(input())
for tc in range(1,T+1):
    fx = list(map(str,input().split()))
    stack = [0] * len(fx)
    top = -1
    for i in fx:
        if i.isdigit():
            top += 1
            stack[top] = int(i)
        else:
            if i == '.':
                if top == 0:  # 스택에 결과값만 남았을 때
                    print(f'#{tc} {stack[top]}')
                else:
                    print(f'#{tc} error')
                break
            elif top < 1:
                print(f'#{tc} error')
                break
            b = stack[top]
            top -= 1
            a = stack[top]
            if i == '+':
                stack[top] = a + b
            elif i == '-':
                stack[top] = a - b
            elif i == '*':
                stack[top] = a * b
            elif i == '/':
                stack[top] = a // b
            else:
                print(f'#{tc} error')  # 알 수 없는 연산자
                break
    # print(f'#{tc} {top}{stack}')

