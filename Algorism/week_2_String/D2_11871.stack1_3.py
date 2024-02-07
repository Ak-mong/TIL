import sys;sys.stdin = open('txt/stack1_3.txt')

t = int(input())
for tc in range(1,t+1):
    n = list(map(str,input()))
    """
    for 문으로 i == a 가 같을 때로 돌린다면?
    연속된 자리가 아니라도 지워진다
    if i == i+1 :
        pop(i) 
        pop(i+1)
    # ABCCB  
    테트리스 처럼 풀어야 된다.
    스택에 쌓아놓고 
    가장 마지막에 들어간 값이랑 이제 넣으려고 하는 값이 같다면 그 값을 pop해버려라 
    """
    top = -1
    flag = 1
    stack = []
    for i in range(len(n)):
        if stack:
            if n[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(n[i])
        else:
            stack.append(n[i])
    print(f'#{tc} {len(stack)}')