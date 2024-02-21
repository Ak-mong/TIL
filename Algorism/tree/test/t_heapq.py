import heapq

# 최소힙만 지원한다.
heap = [7,2,5,3,4,6]
heapq.heapify(heap)
print(heap)
heapq.heappush(heap,1) # 어떤 배열에 무엇을 넣을 것인지
print(heap)
while heap:
    print(heapq.heappop(heap), end=' ')
print()

# 최대합
temp = [7,2,5,3,4,6]
heap2 = []
for item in temp:
    heapq.heappush(heap2, -item)
print(heap2) # 음수지만, 큰 순서로 보인다
heapq.heappush(heap2,-1)
print(heap2)
while heap2:
    print(heapq.heappop(heap2) * -1)