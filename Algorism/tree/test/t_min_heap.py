def enq(node):
    global last
    last += 1 #
    heap[last] = node
    child = last
    parent = child // 2 # 완전이진이니까 가능
    while parent and heap[parent] > heap[child]: # 부모가 있고,
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1 # top 쓰듯이
    p = 1
    c = p * 2 # 대표자식이 왼쪽으로 가정
    while c <= last: # 왼쪽 자식이 있으면
        if c + 1 <= last and heap[c] > heap[c+1]: # 오른쪽 자식이 있고, 오른쪽이 더 작으면 선택 (최소힙)
            c += 1
        # 부모 > 자식 일 때 교체
        if heap[p] > heap[c]:
            heap[p] , heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

arr = [7,2,5,3,4,6]
n = len(arr)
heap = [0]* (n+1) # 완전 이진 트리
last = 0 # 노드가 하나도 없는 상태
for i in range(n):
    enq(arr[i])
print(heap)
for i in range(n):
    print(deq())
