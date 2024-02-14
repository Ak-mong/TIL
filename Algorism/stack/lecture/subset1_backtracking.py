def f(i,k,sums, t): # k개의 원소를 가진 배열A, 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if sums == t: # 모든 원소에 대해 결정하면
        for j in range(k): # 합과 t를 비교하는 반복문
            if bit[j]:  # A[i]가 포함된 경우, bit[i] ==1 이면
                print(A[j], end= ' ')
        print()
    elif i == k : # 모든 원소를 고려했으나 sums != t
        return
    elif sums>t: # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        # for j in range(1,-1,-1): # 1부터 넣고싶다면
        #     bit[i] = j
        #     f(i+1, k, sums+A[i]*j,t)
        bit[i] = 1
        f(i+1, k,sums+A[i],t)
        bit[i] =0
        f(i+1, k,sums,t)
N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
cnt = 0
f(0,N,0,10)
print('cnt: ', cnt)