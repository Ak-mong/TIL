import sys; sys.stdin = open('txt/stack1_2.txt')
t = int(input())

def push():
    global top
    top += 1
def pops():
    global top,flag
    if top ==-1: # 유효성 검사
        flag = 0
        return flag
    top -=1

for tc in range(1,t+1):
    top = -1
    flag = 1
    n = input()
    for i in n:
        if i == '(' or i =='{':
            push()
        elif i == ')' or i =='}':
            pops()
    if top != -1: # 모든 처리가 끝난 후 top이 제자리로 돌아왔냐? == 스택을 전부 소모하지 않았나?
        flag = 0
    print(f'#{tc} {flag}')