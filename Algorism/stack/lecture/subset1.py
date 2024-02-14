def f(i,k,t): # k개의 원소를 가진 배열A, 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if i==k: # 모든 원소에 대해 결정하면
        sums = 0 # 부분집합 원소의 합
        for j in range(k): # 합 구하는 반복문
            if bit[j]: #A[i]가 포함된 경우, bit[i] ==1 이면
                sums += A[j]
        if sums == t:
            for j in range(k): # 합과 t를 비교하는 반복문
                if bit[j]:  # A[i]가 포함된 경우, bit[i] ==1 이면
                    print(A[j], end= ' ')
            print()
    else:
        for j in range(1,-1,-1): # 1부터 넣고싶다면
            bit[i] = j
            f(i+1, k, t)
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] =0
        # f(i+1, k)
N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
cnt = 0
f(0,N,10)
print('cnt: ', cnt)