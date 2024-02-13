import sys; sys.stdin = open('../txt/fastString.txt')
"""
i, cnt = 0,0
for i (n-m +1) (x)
    =>
while i < n-m+1:
    flag = 1
    for j (m):
        if t[i+j != p[j]:
            flag = 0
            break
    if flag:
        cnt += 1
        i = i+m -1
    i += 1

print(n - m*cnt + cnt)
"""

t = int(input())
for tc in range(1,t+1):
    text, pattern = map(str, input().split())
    n,m = len(text), len(pattern)

    i, cnt =0,0
    while i < n - m + 1:
        flag = 1
        for j in range(m):
            if text[i+j] != pattern[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i = i + m -1
        i += 1
    print(f'#{tc} {n-m*cnt + cnt}')