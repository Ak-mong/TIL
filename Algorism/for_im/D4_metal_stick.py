import sys;sys.stdin=open('metal_stick.txt')

'''
쇠막대기를 레이저 n개로 짜르면 n+1개의 조각으로 나온다.
17
24

'''
t= int(input())
for tc in range(1,t+1):
    arr = list(input())
    print(arr)
    lazer = 0
    stack = 0
    for i in range(len(arr)):
        if arr[i] == '(':stack += 1
        else:
            stack -= 1
            if arr[i-1] == '(': lazer += stack
            else: lazer += 1
    print(stack,lazer)