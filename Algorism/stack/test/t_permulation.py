def perm(n,k): # n의 최종단계, k는 현재 단계
    if n == k:
        print(A)
    else:
        for i in range(k,n):
            A[k],A[i] = A[i], A[k]
            perm(n,k+1)
            A[k], A[i] = A[i], A[k]
A = [1,2,3,4]
N = len(A)
perm(N,0)