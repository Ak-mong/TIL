import sys; sys.stdin = open('../txt/stack1_3.txt')

t = int(input())
for tc in range(1, t+1):
    text = input()
    stack = []
    # 문자열 스캔 -> 토큰
    for token in text:
        # 스택이 비어있으면 -> push
        if not stack:
            stack.append(token)
        else:
            # 토큰 피크(맨위를 찍어보는것)한 값을 비교해서 같으면 -> pop
            if token == stack[-1]:
                stack.pop()
            # 그렇지 않으면 push
            else:
                stack.append(token)

    print(f'#{tc} {len(stack)}')

