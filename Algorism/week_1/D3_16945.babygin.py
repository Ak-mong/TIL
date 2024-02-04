import sys; sys.stdin = open('txt/babygin')

t = int(input())
for tc in range(1,t+1):
    cards = list(map(int,input()))
    cnts = [0] * 12 #0~9 까지 10장 + 여분 2장
    for i in cards:
        cnts[i] += 1
    triplet = 0
    run_card = 0
    baby_gin = 0
    num = 0
    while num < 10:
        # # triple 일때
        if cnts[num] >= 3:
            cnts[num] -= 3
            triplet += 1
            continue
        # run_card 판단, 연속된 숫자가 1 이상일 때
        if cnts[num]>= 1 and cnts[num+1]>= 1 and cnts[num+2]>= 1:
            cnts[num] -= 1
            cnts[num+1] -= 1
            cnts[num+2] -= 1
            run_card += 1
            continue
        num += 1
    if triplet + run_card == 2: baby_gin += 1 # while 문이 끝나고 나서 베이비 진 판단
    print(f'#{tc} {baby_gin}')