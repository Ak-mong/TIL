def counting_sort(arr, N, K):
    temp = [0] * N # 정렬된 결과
    counts = [0] * (K+1)
    # 카운팅
    for i in range(N):
        counts[arr[i]] += 1# counts[인덱스] += 1
    # print(counts)
    # 누적
    for i in range(1, K+1):
        counts[i] += counts[i-1]
    # print(counts)
    # 뒤에서 부터 자기 자리 찾아서 정렬하기
    for i in range(N-1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]
    return temp
arr = [ 0, 4, 1, 3, 1, 2, 4, 1]
arr = counting_sort(arr, len(arr), max(arr)) # 배열, 크기, 최대 값

print(arr)