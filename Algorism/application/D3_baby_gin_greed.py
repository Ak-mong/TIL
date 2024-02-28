import sys;sys.stdin= open('txt/baby_gin_greed.txt')
'''
0~9 10개의 숫자카드
4세트
6개 고르기
순열 만들기 -> 반 씩 쪼개서 3개씩 여부 확인
'''
t = int(input())
for tc in range(1,t+1):
    # print('#',tc)
    arr = list(map(int,input().split()))
    a_arr = []
    b_arr = []
    run_a,run_b = 0,0
    triplet_a,triplet_b = 0,0
    babygin_a,babygin_b = 0,0
    for i in range(12):
        if i%2: # 짝수 인덱스 1 3 5 7 ....
            # 2번 선수
            b_arr.append(arr[i])
            if len(b_arr) >= 3:
                b_arr.sort()
                for j in range(2, len(b_arr)):
                    if b_arr[j - 2] == b_arr[j - 1] == b_arr[j]:
                        triplet_b += 1
                    if b_arr[j - 2] == b_arr[j - 1] - 1 == b_arr[j] - 2:
                        run_b += 1
            babygin_b = triplet_b + run_b
            # print(b_arr, run_b, triplet_b)
        else:
            # 1번 선수
            a_arr.append(arr[i])
            if len(a_arr) >= 3:
                a_arr.sort()
                for j in range(2, len(a_arr)):
                    if a_arr[j - 2] == a_arr[j - 1] == a_arr[j]:
                        triplet_a += 1
                    if a_arr[j - 2] == a_arr[j - 1] - 1 == a_arr[j] - 2:
                        run_a += 1
            babygin_a = triplet_a + run_a
            # print(a_arr, run_a, triplet_a)
        if babygin_a < babygin_b:
            flag = 2
        elif babygin_a > babygin_b:
            flag = 1
    if babygin_a == babygin_b:
        flag =0
    print(f'#{tc} {flag}')
