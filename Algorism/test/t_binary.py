# 순차탐색
def binary_search(a,n,key):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) //2
        # 같을 때
        if a[mid] == key:
            return mid # 찾았다
        elif a[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1 # 못찾았다


arr = [2,4,7,9,11,19,23]
n = len(arr)
key = 23
print(binary_search(arr,n,key))
