# 순차탐색
def seq_search(a,n,key):
    for i in range(n):
        if a[i] == key:
            return i
    return -1

arr = [4,9,11,23,2,19,7]
n = len(arr)
key = 19
print(seq_search(arr,n,key))
