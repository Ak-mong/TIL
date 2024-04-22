import sys
input = sys.stdin.readline

# 11723 집합 실버 5
n = int(input())
S = set()
for _ in range(n):
    arr = list(map(str,input().split()))
    # print(arr)
    # print(S)
    F = arr[0]
    if len(arr) == 2: V = int(arr[1])
    if F == 'add' and V not in S:
        S.add(V)
    elif F == 'remove' and V in S:
        S.remove(V)
    elif F == 'check':
        if V in S:
            print(1)
        else:
            print(0)
    elif F == 'toggle':
        if V in S:
            S.remove(V)
        else:
            S.add(V)
    elif F == 'all':
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        # print(S)
    elif F == 'empty':
        S.clear()