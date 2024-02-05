import sys; sys.stdin = open('txt/palindrome2')
# for 문 3개가 필요하다.
t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]
    # print(n,m, arr)
    new_word = []
    for i in range(n):
        for j in range(n-m+1):
            flag = 1
            for k in range(m//2):#회문 비교
                # 가로 확인해서 못 찾으면 flag =0
                if arr[i][j+k] != arr[i][j+m-1-k]:
                    flag = 0
                    break
            if flag:
                for x in range(m):
                    new_word += arr[i][j+x] #JAEZN NZEAJ
    #세로 확인해서 찾으면 1
    for p in range(n):
        for q in range(n-m+1):
            flag = 1
            for r in range(m // 2):  # 회문 비교
                # 세로 확인해서 못 찾으면 flag =0
                if arr[q+r][p] != arr[q + m - 1 - r][p]:
                    flag = 0
                    break
            if flag:
                for x in range(m):
                    new_word += arr[q + x][p]  # JAEZN NZEAJ

    new_word = ''.join(new_word)
    print(f'#{tc} {new_word}')
