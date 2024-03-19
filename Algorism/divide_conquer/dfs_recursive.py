arr = [i for i in range(1,4)]
path = [0] * 3

# 조합
# 123,132, 213, 231, 312 ,321


def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑아을 때 까지 반복
    if level == 3:
        return

    # 들어가기 전 다음 재귀 호출 갔다와서 할 로직
    # 기본 코드
    '''
    path[level] = arr[0]
    dfs(level + 1)

    path[level] = arr[2]
    dfs(level + 1)
    '''
    # 기본 코드를 반복문으로 변경
    # 갈 수 있는 후보군
    for i in range(len(arr)):
        # 여기는 못가 ! (가지치기)
        # 갈 수 없을 때 조건을 거는 것이 조건이 까다로울 수록 좋음

        # 조건 1~~~
        if arr[i] in path:
            continue
        if 조건 2:
            continue

        path[level] = arr[i]
        dfs(level+1)
        # 갔다와서 할 로직
        # 기존 방문을 초기화
        path[level] = 0

dfs(0)