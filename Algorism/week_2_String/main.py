"""
23969 알고리즘 수업 - 버블 정렬 2

bubble_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2
        for i <- 1 to last - 1
            if (A[i] > A[i + 1]) then A[i] <-> A[i + 1]  # 원소 교환
}
"""
n,k = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
for i in range(n-1,0,-1): #n-1 to 1 리스트를 n-1까지 비교하기
    for j in range(i): #0 to i 0~ i 까지 비교해서
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            cnt += 1
            if cnt == k:
                print(*arr)
if cnt < k:
    print(-1)