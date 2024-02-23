import sys;sys.stdin =open('input.txt')

def makeTree(node):
    global num
    # 재귀로 할 거다.
    if node <= n:
        #후위
        makeTree(node*2) #왼쪽 자식

        makeTree(node*2+1) #오른 쪽 자식
        tree[node] = arr[num]  # 부모
        num += 1
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    # print()
    # 이진 최소값 구하기 => 재귀
    # 일단 tree선언
    tree = [0] * (n+1)
    num = 0 # 노드 인덱스에 들어갈 arr[num] 값
    makeTree(1) # 노드 번호는 루트가 1
    print(tree)
