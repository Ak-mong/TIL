maxsize = 100
stack = [0] * maxsize
top = -1
stack[top] = 1
#push
top += 1
stack[top] = 1
#push
top += 1
stack[top] = 2

#pop
if top != -1: #필수 요소
    item = top
    print(item)
    top -= 1