import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

# 13116 30번 실버4
t = int(input())
for _ in range(t):
    A,B = map(int,input().split())
    arr_a = []
    arr_b = []

    while A >=1:
        arr_a.append(A)
        if A%2:
            A = A-1
        A //= 2
    while B >= 1:
        arr_b.append(B)
        if B%2:
            B = B-1
        B //= 2
    # print(arr_a,arr_b)
    max_v = 0
    for i in arr_a:
        if i in arr_b and max_v < i:
            max_v = i
    print(max_v*10)