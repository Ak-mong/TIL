import sys; sys.stdin = open('../txt/password.txt')

t = 10
for tc in range(1,t+1):
    no = int(input())
    q = list(map(int,input().split()))

    cnt = 0
    while True:
        tmp = q.pop(0)
        tmp -= cnt % 5 +1
        if tmp < 0: tmp = 0
        q.append(tmp)
        cnt += 1
        if tmp == 0:
            break

    print(f'#{tc}', *q)
