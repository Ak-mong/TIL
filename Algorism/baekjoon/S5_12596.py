import sys;sys.stdin=open('input.txt')
'''
같은 숫자가 있다면 그거를 뺴자
'''
# def find_couple(arr):
#     if arr:
#         c = arr.pop()
#         stack.append(c)



t = int(input())
for tc in range(1,t+1):
    g = int(input())#게스트
    arr = list(map(int,input().split()))
    # stack = [arr.pop()]
    arr.sort()
    stack = []
    result = arr[0]
    # stack.append(arr.pop())
    while len(arr) > 1:
        value = arr.pop()
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == value:
                arr.pop(i)
                break
        else:
            result = value
            break

    # count = [0] * (2147483647+1)
    # for i in range(g):
    #     count[arr[i]] += 1
    # print(count)
    # stack = []
    # top = -1
    # stack.append(arr[top])
    # while stack:
    #     if stack[top] == arr[top]:
    #         stack.pop()
    #         top -= 1
    #     else:
    #         stack.append(arr[top])
    #     top += 1
    #
    #     if len(stack) == 1:
    #         break
    # print(stack[top])




    print(f'Case #{tc}: {result}')
