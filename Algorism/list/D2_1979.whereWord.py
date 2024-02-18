import sys;sys.stdin = open('txt/whereword.txt')
T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # print(arr)
    """
    흰색이 1
    """
    word_cnt = 0 # 가능한 단어 갯수 초기화
    for i in range(n):
        cnt = 0 # 개수 초기화
        for j in range(n): # 가로 검사
            if arr[i][j] == 1:
                cnt += 1
            # 검은색을 만났거나 or 벽에 닿았을 때
            if arr[i][j] == 0 or j == n-1:
                # 길이만큼 있으면?
                if cnt == k:
                    word_cnt +=1
                cnt = 0
                # break # 해당 가로는 더 볼거 없다
        # 세로검사
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            # 검은색을 만났거나 or 벽에 닿았을 때
            if arr[j][i] == 0 or j == n-1:
                # 길이만큼 있으면?
                if cnt == k:
                    word_cnt +=1
                cnt = 0
                # break # 해당 가로는 더 볼거 없다
    print(f'#{tc} {word_cnt}')

    """
    0 으로 이루어진 길이가 딱 k 만큼 되야 된다.
    k 보다 많아도 적어도 안된다.
    2방향만 보면 된다.
    """
    '''
    ok_cnt = 0 # 단어들어갈수 있는 객수
    for i in range(n):
        len_ok = 0 # 길이 맞는지 카운트
        for j in range(n): # 행 검사
            if arr[i][j] == 1: # 흰색 칸이라면
                len_ok += 1
            if arr[i][j] == 0 or j == n-1: # 검은칸이거나 j가 끝에 다다랐거나
                if len_ok == k: # k의 길이와 같을 때
                    ok_cnt += 1
                len_ok = 0 # 행으로 검사가 끝났으니 0으로 초기화
        for j in range(n):  # 열 검사
            if arr[j][i] == 1:  # 흰색 칸이라면
                len_ok += 1
            if arr[j][i] == 0 or j == n - 1:  # 검은칸이거나 j가 끝에 다다랐거나
                if len_ok == k:  # k의 길이와 같을 때
                    ok_cnt += 1
                len_ok = 0 # 열으로 검사가 끝났으니 0으로 초기화

            # if arr[i][j] == 0 and arr[i+1][j] == 0 and arr[i+2][j] == 0:
            # elif arr[i][j] == 0 and arr[i][j] == 0 and arr[i][j] == 0:
    print(ok_cnt)
'''