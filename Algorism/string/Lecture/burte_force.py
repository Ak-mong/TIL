

t = int(input())
def f(pat, txt, m, n):
    for i in range(n-m+1):   #text에서 비교 시작 위치0 ~ n-m
        for j in range(m):
            if txt[i+j] != pat[j]: #불일치면 다음 시작위치로
                break
        else: #for 문이 잘 완료 됐다면? #패턴 매칭에 성공하면
            return 1
    # 모든 위치에서 비교가 끝난경우 # 패턴 매칭에 실패한 경우
    return 0
for tc in range(1,t+1):
    pat = input()
    txt = input()
    m = len(pat)
    n = len(txt)

    ans = f(pat, txt, m, n)

    print(f'#{tc} {ans}')

