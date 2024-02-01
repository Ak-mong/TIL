import sys; sys.stdin = open('txt/specialindexing.txt')

def max_value(arr):
    max_v = arr[0]
    for i in range(len(arr)):
        if max_v < arr[i]:
            max_v = arr[i]
    return max_v
def min_value(arr):
    min_v = arr[0]
    for i in range(len(arr)):
        if min_v > arr[i]:
            min_v = arr[i]
    return min_v

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    new_arr = []
    """while len(arr) > 0:
        max_val = max_value(arr)
        arr.remove(max_val)
        new_arr.append(max_val)

        min_val = min_value(arr)
        arr.remove(min_val)
        new_arr.append(min_val)
    print(f'#{tc} {new_arr}')
    """
    for i in range(n):
        idx = i
        if i % 2: #홀수일때 작은 값
            for j in range(i+1,n):
               if arr[idx] > arr[j]:
                   idx = j
            arr[i], arr[idx] = arr[idx],arr[i]
        else: #짝수일때 큰 값
            for j in range(i+1,n):
                if arr[idx] < arr[j]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]

    print(f"#{tc} {' '.join(map(str,arr[:10]))}")

    # 인덱스[0 ,1,2,3,4,5,6,7,8,9]
    # 실제값[10,9,8,7,6,5,4,3,2,1]
