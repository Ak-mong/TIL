import sys; sys.stdin = open('../txt/4calc.txt')
'''
poset(v)
    if ch1[v] == 0 and ch2[v] == 0: # 잎노드
        return num[v]
    else:                           # 가지노드
        l = post(ch1[v])
        r = post(ch2[v])
        num[v] = calc (op[v],l,r)
        return num[v]
    '''
def calc(op,l,r):
    if op == '+':
        return l+r
    elif op == '-':
        return l-r
    elif op == '*':
        return l*r
    elif op == '/':
        return l/r

def postorder(v):
    # 잎노드
    if ch1[v] == 0 and ch2[v] == 0: # 자식이 없다면
        return num[v]
    # 가지노드
    else:
        l = postorder(ch1[v])
        r = postorder(ch2[v])
        num[v] = calc(op[v],l,r)
        return num[v]
t = 10
for tc in range(1,t+1):
    n = int(input())
    op = [''] * (n+1)
    ch1 = [0] * (n+1)
    ch2 = [0] * (n+1)
    num = [0] * (n+1)

    for i in range(n):
        tmp = list(input().split())
        idx = int(tmp[0])
        # 연산자
        if tmp[1] == '+' or tmp[1] == '-' or tmp[1] == '*' or tmp[1] == '/':
            op[idx] = tmp[1]
            ch1[idx] = int(tmp[2])
            ch2[idx] = int(tmp[3])
        else: # 피 연산자
            num[idx] = int(tmp[1])
    ans = postorder(1)
    print(f'#{tc} {int(ans)}')