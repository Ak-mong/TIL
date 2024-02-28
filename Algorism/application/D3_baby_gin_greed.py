import sys;sys.stdin= open('txt/baby_gin_greed.txt')
'''
0~9 10개의 숫자카드
4세트
6개 고르기
순열 만들기 -> 반 씩 쪼개서 3개씩 여부 확인
'''
def baby_gin(arr):
    # run판단
    for x in range(len(arr)-2):
        if arr[x] >= 1 and arr[x+1] >= 1 and arr[x+2]>= 1:
            return True
    # triplet 판단
    for y in range(len(arr)):
        if arr[y] == 3:
            return True
    return False

def whoisWin():
    for i in range(6):
        count_a[arr[i * 2]] += 1  # 홀수 인덱스
        count_b[arr[i * 2 + 1]] += 1  # 짝수 인덱스
        if baby_gin(count_a):
            return 1
        elif baby_gin(count_b):
            return 2
    return 0

t = int(input())
for tc in range(1,t+1):
    arr = list(map(int,input().split()))
    n = len(arr)
    card = 10
    count_a = [0]*10
    count_b = [0]*10

    print(f'#{tc} {whoisWin()}')
    # print(count_a)
    # print(count_b)
    # print(result)






