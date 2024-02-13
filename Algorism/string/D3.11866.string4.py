import sys;sys.stdin = open('txt/string4.txt')
t = int(input())
for tc in range(1,t+1):
    """
    리스트로 만들어서 하나씩 for문으로 돌아가면서 비교해야되나?
    아니면 텍스트 그대로 쓸 수 있나?
    """
    # 리스트로 만들어서 해보기
    patten = list(map(str,input()))
    text = list(map(str,input()))
    n = len(patten)
    m = len(text)
    # 리스트로 비교하기
    sum_v = 0
    for i in patten: #패턴을 가지고 text에 비교하자
        count = 0
        for j in text:
            if j == i:
               count +=1 # 같은게 있으면 카운트 업
        if sum_v < count:
            sum_v = count
    print(f'#{tc} {sum_v}')