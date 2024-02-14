# 부분집합의 합이 10인 경우를 출력하시오
def solution(n, cursum):
    if cursum == 10:
        for i in range(n):
            if A[i]:
                print(arr[i], end=' ')
        print()

def powerset(n,k, cursum): #n은 최종단계, k는 현재단계
    global cnt
    cnt += 1
    ################
    if cursum > 10: return # 유망하지않으니 되돌아가라
    ################
    if n == k:
        solution(n, cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum+arr[k])
        A[k] = 0
        powerset(n, k + 1, cursum)

arr = list(range(1,11))
N = len(arr)
cnt = 0
A = [0] * N # (0,1)로 포함여부를 저장
powerset(N,0,0)
print(cnt)