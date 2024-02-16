Q = []

# enQ
Q.append(1) # O(1)
Q.append(2)
Q.append(3)
print(Q) # [1,2,3]
print(f'peak : {Q[0]}')

# deQ
while Q:
    print(Q.pop(0)) # O(n) == 비효율적이다.
print(Q) # []