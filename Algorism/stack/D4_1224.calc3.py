import sys;
sys.stdin = open('txt/calc3.txt')

icp_prior = {'+': 1, '*':2, '(':3}
isp_prior = {'+': 1, '*':2, '(':0}

def before_calc(str):
    new_str= ''
    stack = []
    top = -1
    for tk in str:
        if tk.isdigit():
            new_str += tk
        else:
            # 여는 괄호 or 연산자가 stack[top]의 우선순위보다 넣는 부호가 우선순위가 높을 경우
            if tk == '(' or (tk in '*+' and isp_prior[stack[top]] < icp_prior[tk]):
                top += 1
                stack.append(tk)
            # 연산자인데 우선순위가 stack에 있는 우선순위보다 낮을 경우
            elif tk in '*+' and isp_prior[stack[top]] >= icp_prior[tk]:
                while isp_prior[stack[top]] >= icp_prior[tk]:
                    top -= 1
                    new_str += stack.pop()
                # 필요할 만큼 연산자를 꺼냈으니, 현재 들고있는 연산자를 다시 stack에 넣기
                top += 1
                stack.append(tk)
            # 닫는 연산자가 나왔을 때
            elif tk == ')':
                while stack[top] != '(':
                    top -= 1
                    new_str += stack.pop()
                # 닫는 연산자는 stack추가하지 않아도 된다, 그리고 pop한 '(' 도 추가하진 않는다.
                top -= 1 # 하지만 top은 하나 더 줄었음
                stack.pop()
    # print('top',top)
    return new_str

def calc_str(input_str):
    stack = []
    top = -1
    for tc in input_str:
        if tc.isnumeric():
            stack.append(int(tc))
            top += 1
        elif tc == '*':
            b = stack.pop()
            top -= 1
            a = stack.pop()
            stack.append(a * b)
        elif tc == '+':
            b = stack.pop()
            top -= 1
            a = stack.pop()
            stack.append(a + b)

    # print('top+', top)
    return stack[top]
T = 10
for tc in range(1,T+1):
    N = int(input())
    # calc_arr = list(map(str,input()))
    calc_arr = input()
    # print(calc_arr)
    # calc(before_calc(calc_arr,N))
    # print(before_calc(calc_arr))
    print(f'#{tc} {calc_str(before_calc(calc_arr))}')