def bubble_sort(arr,N):
    for i in range(N-1, 0, -1): # 4 3 2 1
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(*arr)
arr = [ 55, 7, 78, 12, 42]
print(arr)
bubble_sort(arr, len(arr))
print(arr)

