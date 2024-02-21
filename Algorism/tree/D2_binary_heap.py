import sys;sys.stdin = open('txt/binary_heap.txt')
def min_heap(node):
    global last
    last += 1
    heap[last] = arr[node]
    child = last
    parent = child // 2 # 완전 이진 트리라서 가능
    if node<0:
        return
    while parent and heap[parent] > heap[child]: # 부모가 있는데 부모가 자식보다 크다면?
        heap[parent] , heap[child] = heap[child],  heap[parent] # 교환
        child = parent
        parent = child//2
def binar_sum():
    value = 0
    node = n //2 # 3 1 0
    while node:
        value += heap[node]
        node //= 2
    return value


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    heap = [0] * (n+1)
    # 2 5 가 더해져야된다.
    # 트리부터 만들기
    # 마지막 인수
    last = 0
    for i in range(0,n):
        min_heap(i)
    print(f'#{tc} {binar_sum()}')