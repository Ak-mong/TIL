import sys; sys.stdin = open('txt/fastString.txt')
T =int(input())
for tc in range(1,T+1):
    A,B = map(str,input().split())
    a_len = len(A)
    b_len = len(B)
    # a sa k u sa 5번만에 된다
    cnt = 0
    i = 0
    while i < a_len:
        if B == A[i:i+b_len]: # 0 1 2 3 인덱스 비교
            cnt += 1
            i += b_len
        else:
            i +=1
    print(cnt)
    print(f'#{tc} {a_len - b_len * cnt + cnt}')
