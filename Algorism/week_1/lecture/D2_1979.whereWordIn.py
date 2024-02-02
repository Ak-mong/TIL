import sys; sys.stdin = open('../txt/whereword in.txt')

t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) + [0] for _ in range(n)] + [[0] * (n+1)] #0 추가 시키는 코드
    print(arr)
    n += 1
    # 가로, 세로로 연속한 1의 개수가 k인 경우를 구하는 것
    ans = 0
    for i in range(n):
        cnt = 0 # i 행에서 연속한 1의 개수
        for j in range(n):
            if arr[i][j]:
                cnt += 1
            else: # arr[i][j] == 0
                if cnt == k:
                    ans += 1
                cnt = 0
    print(f'#{tc} {ans}')