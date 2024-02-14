# 순열 만들기
"""
P[j] : j 행에서 선택한 열
s = 0
for j : 0 -> N-1
    s += A[j][p[j]]
"""
def f(i,k, sums):
    global min_v, cnt
    cnt += 1
    if i==k:
        # print(*P)
        if min_v > sums:
            min_v = sums
    elif sums >= min_v:
        return
    else:
        for j in range(i,k): #P[i] 자리에 올 원소 P[j]
            P[i],P[j] = P[j],P[i] # P[i] <-> P[j]
            f(i+1, k, sums + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]  # 교환전으로 복구, 골고루 잘 섞기 위함

N = 3
arr = [
[2,1,2],
[5,8,5],
[7,2,2]
]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0,N, 0)
print(min_v,cnt)