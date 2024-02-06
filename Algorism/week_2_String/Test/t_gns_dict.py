import sys; sys.stdin = open('../txt/GNS.txt')

digits = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
t = int(input())
for tc in range(1,t+1):
    tmp = input()
    arr = list(map(str,input().split()))
    # 카운팅
    cnts = {}
    for item in arr:
        if cnts.get(item):
            cnts[item] += 1
        else:
            cnts[item] = 1
    result = ''.join(list(map(lambda n:(n + ' ') * cnts[n], digits)))
    # 출력
    print(f'#{tc}')
    print(result)