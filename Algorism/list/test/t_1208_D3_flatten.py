import sys; sys.stdin = open('../txt/flatten')
T = 10
def get_m(arr,N):
    max_idx = min_idx = 0
    for i in range(N):
        if arr[max_idx] < arr[i]:
            max_idx = i
        if arr[min_idx] > arr[i]:
            min_idx = i
    return max_idx, min_idx

for tc in range(1, T+1):
    dump_cnt = int(input())
    N = 100 # 고정 배열의 크기
    arr = list(map(int, input().split()))

    # 덤프 횟수만큼 평탄화
    for i in range(dump_cnt):
        max_idx, min_idx = get_m(arr,N)
        arr[max_idx] -= 1
        arr[min_idx] += 1
    # 반드시 최종 덤프 후에 최고점과 최저점의 차이를 반환
    max_idx,min_idx = get_m(arr,N)
    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')