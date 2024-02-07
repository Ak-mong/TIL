# 주의할 점, 스택의 크기를 아끼지 말자, 절대로 꽉차게 만들지 말자
# isEmpty는 체크하지만(pop할떄), isFull은 체크 안하게
# 리스트를 고정적으로 만들면 늘릴 방법이 없기 때문
def push(item):
    global top
    if top > maxsize -1:
        print('overflow') # 넘쳐버렸다, 실제로 여기로 들어오면 절대 안된다.
        return 0
    else:
        top += 1
        stack[top] = item

def pops():
    global top
    if top ==-1: # 항상 체크해줘야됨
        print('stack is empty')
        return
    else:
        """ 
        pop 이 이루어지고 나서 top을 하나 줄여야 되는데,
        return 다음에 top을 줄일수 없기 때문에 result에 값을 넣어놓고 result를 리턴함
        """
        result = stack[top]
        top -= 1
        return result


maxsize = 100
stack = [0] * maxsize
top = -1

push(1);push(2);push(3)
item = pops()
print(item)

while top != -1: # 굳이 pop한 것을 지울 필요는 없다.
    print(pops()) # 3 \n 2 \n 1

print(stack) # [1,2,3, ...]
