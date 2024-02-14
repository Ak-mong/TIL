def perm(n,k, cursum): # n의 최종단계, k는 현재 단계, 현재 합
    global ans
    if ans < cursum: return # 가지치기
    if n == k:
        if ans > cursum: ans = cursum
        print(A)
    else:
        for i in range(k,n):
            A[k],A[i] = A[i], A[k]
            perm(n,k+1, cursum + A[k])
            A[k], A[i] = A[i], A[k]
A = [1,2,3]
N = len(A)
ans = 6
perm(N,0,0)
