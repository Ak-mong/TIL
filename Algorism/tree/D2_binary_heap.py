import sys;sys.stdin = open('txt/binary_heap.txt')
def min_heap(node):
    global last
    last += 1
    heap[last] = arr[node]
    child = last
    parent = child // 2 # 완전 이진 트리라서 가능
    if node <= n: # 노드 번호의 인덱스는 작아야된다.
        if heap[last] > heap[last +1]:
            heap[last],heap[last+1] = heap[last+1], heap[last]

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
    print(heap)