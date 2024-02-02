def binary_search(arr, N, key):
    start = 0 # 구간 초기화
    end = N -1
    while start <= end: # 검색 구간이 유효하면 반복
        mid = (start+end) // 2 # 중앙원소 인덱스
        if arr[mid] == key:
            return mid # 검색 완료 True
        elif arr[mid] > key: # 중앙 값이 키보다 크면
            end = mid - 1
        else: # 중앙 값이 키보다 작으면
            start = mid + 1
    return -1 # 검색 실패 -1, False, x 등등
            




