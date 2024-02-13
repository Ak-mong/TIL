def powerset(n,k): #최종 단계, 현단계
    ### 가지치기 ###
    if n == k:
        # 이 부분은 항상 바뀔 수 있다.
        print(bit, end=' ')
        for i in range(n):
            if bit[i] == 1:
                print(arr[i], end=' ')
        print()
    # 이부분이 실제
    else:
        bit[k] = 1
        powerset(n,k+1)
        bit[k] = 0
        powerset(n,k+1)

arr = [1,2,3]
N = len(arr)
bit = [0]*N
powerset(N,0)