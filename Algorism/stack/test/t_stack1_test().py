import sys; sys.stdin = open('../txt/stack1_2.txt')


def solve(text):
    stack = []
    # 문자열을 문자로 하나씩 스캔한다.
    for token in text:
        # 왼쪽괄호
        if token == '(' or token == '{':
            stack.append(token)
        # 오른쪽괄호
        elif token == ')' or token == '}':
            # 스택이 비어있으면 return 0
            if not stack:  # len(stack) == 0
                return 0
            else:
                tmp = stack.pop()  # pop
                # 짝검사 return 0
                if token == ')' and tmp != '(':
                    return 0
                elif token == '}' and tmp != '{':
                    return 0

    # 스캔완료후 스택에 남아 있으면 return 0
    if stack: return 0

    return 1


T = int(input())
for tc in range(1, T + 1):
    text = input()
    print(f'#{tc} {solve(text)}')