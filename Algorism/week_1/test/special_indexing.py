import sys; sys.stdin = open('../txt/specialindexing.txt')
def selection(arr,n):
    for i in range(10): #0<= i < n-1
        idx = i
        if i%2: # 홀수 일때
            for j in range(i+1,n): #i+1<= j <n
                if arr[idx] > arr[j]:
                    idx = j
        else: #짝 수 일때
            for j in range(i+1,n): #i+1<= j <n
                if arr[idx] < arr[j]:
                    idx = j
        arr[i],arr[idx] = arr[idx],arr[i]

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    selection(arr,n)

    print(f'#{tc}',*arr[:10])