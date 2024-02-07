import sys; sys.stdin = open('txt/stack1.txt')
t = int(input())

def push():
    global top
    top += 1
def pops():
    global top,flag
    if top == -1:
        flag = 0
        return flag
    top -= 1

for tc in range(1,t+1):
    n = input()
    flag = 1
    top = -1
    for i in n:
        if i == '(':
            push()
        elif i ==')':
            pops()
    if top != -1:
        flag = 0
    print(f'#{tc} {flag}')
