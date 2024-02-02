import sys; sys.stdin = open('../txt/binary.txt')
def binary_search(a,n,key):
    s,e = 1,n
    cnt= 0
    while s<= 0:
        cnt += 1
        m = (s+e)//2
        if a[m] == key:
            return cnt
        elif a[m] > key:
            e = m
        else:
            s = m
    return -1


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    arr = [0] + list(range(1, P + 1))

    a = binary_search(arr, P, A)
    b = binary_search(arr, P, B)

    ans = '0'
    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'

    print(f'#{tc} {ans}')