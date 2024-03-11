N, M = map(int,input().split())
chess = [list(input()) for _ in range(N)]
count = []

for a in range(N-7):
    for b in range(M-7):
        black = 0
        whilte = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 짝수면 시작점과 색깔이 같다
                    if chess[i][j] != 'W':
                        black += 1
                    if chess[i][j] != 'B':
                        whilte += 1
                else: # 홀수면 시작점과 색깔이 다르다
                    if chess[i][j] != 'B':
                        black += 1
                    if chess[i][j] != 'W':
                        whilte += 1
        count.append(min(black, whilte))

print(min(count))