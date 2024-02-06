import sys;sys.stdin =open('txt/palindrome1.txt')
t = 10
for tc in range(1,t+1):
    n = int(input()) #찾아야되는 회문 길이
    arr = [list(input()) for _ in range(8)] #회문판
    # print(arr)
    count = 0
    for i in range(8-n+1):
        for j in range(8-n+1):
            flag = 1
            for p in range(n//2):
                # 가로
                if arr[i][j] != arr[i][j+p]:
                    flag = 0
                    break
            if flag == 1:
                count += 1
                # 세로
            for q in range(n//2):
                if arr[i][j] != arr[i+q][j]:
                    flag = 0
                    break
            if flag == 1:
                count += 1
            count += 1

    print(count)
