"""
bubble_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2
        for i <- 1 to last - 1
            if (A[i] > A[i + 1]) then A[i] <-> A[i + 1]  # 원소 교환
}
"""
n,k = map(int,input().split())
arr = list(map(int,input().split()))
max_v = 0
for i in range(n-1,n-1-k,-1): #n-1 to 1
    for j in range(i): #0 to I
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)