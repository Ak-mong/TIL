def selection_sort(arr,N):
    for i in range(N-1): # 구간이 시작 i, 2개의 원소가 남을 때 까지
        min_idx = i # 구간의 최소값 위치 min_idx, 첫 원소를 최소로 가정
        #min_v 필요없다. 위치값만 있으면 된다.
        for j in range(i+1, N):# 실제 최솟값을 찾을 위치 j
            if arr[min_idx] > arr[j]: # 더 작은 값이 있으면 바꿔줘
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]# 최소값을 구간의 맨 앞으로 이동
    return

N = 5
arr= [1, 3, 2, 5, 4]
print(arr)
selection_sort(arr, N)
print(arr)




