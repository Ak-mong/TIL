import sys; sys.stdin = open('../txt/GNS.txt')

digits = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
t = int(input())
for tc in range(1,t+1):
    tmp = input()
    arr = list(map(str,input().split()))
    cnts = [0] * 10
    for item in arr:
        for j in range(10):
            if item == digits[j]:
                cnts[j] +=1

    # 출력
    print(f'#{tc}')
    for i in range(10):
        for j in range(cnts[i]):
            print(digits[i], end=' ')
    print()