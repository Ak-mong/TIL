# front, rear 이용
Q = [0] * 10
front = rear = -1

# enQ
rear += 1
Q[rear] = 1
rear += 1
Q[rear] = 2
rear += 1
Q[rear] = 3
print('before',front, rear,Q) # -1 2 [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
print(f'peek : {Q[front+1]}') # Qpeek # 1


# deQ
while front != rear:
    front += 1
    print(Q[front])
print('after',front, rear,Q) #  2 2 [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
