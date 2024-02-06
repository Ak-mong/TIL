import sys;sys.stdin =open('txt/palindrome1.txt')
t = 10
for tc in range(1,t+1):
    n = int(input()) #찾아야되는 회문 길이
    length = 8
    arr = [list(input()) for _ in range(length)] #회문판
    count = 0 # 회문의 수를 구하기 위해 초기화
    # 가로
    for i in range(length):
        for j in range(length - n + 1): # 9- 찾는 길이
            flag = 1
            for p in range(n):
                # 가로
                if arr[i][j+p] != arr[i][j + n - 1 - p]: # 한 칸씩 갈때마다 계속 비교해 나간다
                    flag = 0
                    break
            if flag == 1:
                count += 1
    # 세로
    for i in range(length -n +1): # 9- 찾는 길이
        for j in range(length):
            flag = 1
            for q in range(n):
                # 세로
                if arr[i+q][j] != arr[i + n - 1 - q][j]: # 한 칸씩 갈때마다 계속 비교해 나간다
                    flag = 0
                    break
            if flag == 1:
                count += 1
    print(f'#{tc} {count}')
