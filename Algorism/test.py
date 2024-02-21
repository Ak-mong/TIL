import sys;sys.stdin =open('input.txt')
# subtree
t =int(input())
for tc in range(1,t+1):
    E, N = map(int,input().split()) # 간선, 루트 노드 N
    arr= list(map(int,input().split())) # 노드 연결 정보
          # for _ in range(E+1): #총 노드 개수 E+1
    tree = [0] * (E+2) # 1차원 배열 트리
    for i in range(E):
        tree[arr[i*2]] = arr[i*2+1]
    print(tree)
