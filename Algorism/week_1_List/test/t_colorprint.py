import sys; sys.stdin = open('../txt/color_print.txt')
import pprint

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    #  색칠하기
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1,c2+1):
                arr[i][j] += color
    # 겹쳐진 칸수(3)를 카운트
    # pprint.pprint(arr)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3:
                cnt +=1
    print(f'#{tc} {cnt}')
