import sys;
sys.stdin =open('input.txt')

# 9012 괄호

# def stacks():

t = int(sys.stdin.readline().strip())
for tc in range(t):
    arr = list(sys.stdin.readline().strip())
    # print(arr)
    stack = []
    flag = 'YES'
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                flag = 'NO'
                break
    if stack: flag = 'NO'
    print(flag)
