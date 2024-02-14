import sys; sys.stdin = open('../txt/calc3.txt')
icp = {'+': 1,'-': 1, '*':2,'/':2, '(':3}
isp = {'+': 1,'-': 1, '*':2,'/':2, '(':0}
def infix_to_postfix(infix):
    stack = []
    result = ''
    # 입력받은 중위표기식에서 토큰을 읽는다.
    for tok in infix:
        # 토큰이 피연산자이면 토큰을 출력한다.
        if '0'<= tok <= '9':
            result += tok # 단순 연결
            # 토큰이 연산자(괄호포함)일 때,
        elif tok == '(' or tok == '+' or tok =='-' or tok =='*' or tok =='/': # # tok in '(+_*/'
            # 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push 하고
            # 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop
                # 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
            if stack:
                while icp[tok] <= isp[stack[-1]]:
                    result += stack.pop()
                    if not stack: break
                # stack.append(tok)
            # else:
            #     stack.append(tok)
            stack.append(tok) # 스택이 비어 있거나 or while 을 탈출한 경우 // 위 3줄을 대체하는 코드
        # 토큰이 오른쪽 괄호 `‘)’`이면 스택 top에 왼쪽 괄호 `‘(’`가 올 때까지 스택에 pop 연산을 수행하고 pop 한 연산자를 출력한다. `왼쪽 괄호`를 만나면 pop만 하고 출력하지는 않는다.
        elif tok == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    #스택에 남아 있는 연산자를 모두 pop하여 출력한다.
    while stack:
        result += stack.pop()
    return result
def calc(postfix):
    stack = []
    for tok in postfix:
        # 1. 피연산자를 만나면 스택에 push 한다.
        if '0' <= tok <= '9':
            stack.append(int(tok))
        # 2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push 한다.
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if tok == '+':
                stack.append(op1 + op2)
            if tok == '-':
                stack.append(op1 - op2)
            if tok == '*':
                stack.append(op1 * op2)
            if tok == '/':
                stack.append(op1 / op2)
    # 3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.
    return stack.pop()

T = 10
for tc in range(1,T+1):
    N = int(input())
    infix = input()
    postfix = infix_to_postfix(infix)
    # print(postfix)
    print(f'#{tc} {calc(postfix)}')