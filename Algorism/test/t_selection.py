def selection_sort(arr,n):
    for i in range(n-1):
        #최고값 인덱스
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        #교체
        arr[i], arr[min_idx] = arr[min_idx] , arr[i]

arr = [64,25,10, 22,11]
n = len(arr)
selection_sort(arr, n)
print(arr)