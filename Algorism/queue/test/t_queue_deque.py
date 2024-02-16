from collections import deque

Q = deque()

# enQ
Q.append(1) # O(1)
Q.append(2)
Q.append(3)
print(Q) # [1,2,3]
print(f'peak : {Q[0]}')

# deQ
while Q:
    print(Q.popleft()) # O(1) ==> 효율적이다.
print(Q) # []