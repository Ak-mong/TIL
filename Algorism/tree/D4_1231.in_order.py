import sys;sys.stdin = open('txt/in_order.txt')
T = 10
def in_order(n):
    global word
    if n: # n이 존재한다면
        in_order(left[n]) # 왼쪽 자식 노드
        word += tree[n] # root
        in_order(right[n]) #오른쪽 자식노드

for tc in range(1,T+1):
    N = int(input())
    # arr = [input().split() for _ in range(N)]
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    word = ''
    for i in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
        if len(arr) >= 3:
            left[int(arr[0])] = int(arr[2]) # 정수로 바꿔야 된다.
        if len(arr) == 4:
            right[int(arr[0])] = int(arr[3]) # 정수로 바꿔야된다.
        # for j in range(len(arr)): # 0~6
        #     parent = arr[0]
        # if len(arr[i])
    # print(tree)
    # print(left)
    # print(right)
    in_order(1)
    print(f'#{tc} {word}')
    # for i in arr: print(i)



