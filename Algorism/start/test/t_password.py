import sys; sys.stdin = open('../txt/password.txt')
mapping = {
     '0001101': 0,
     '0011001': 1,
     '0010011': 2,
     '0111101': 3,
     '0100011': 4,
     '0110001': 5,
     '0101111': 6,
     '0111011': 7,
     '0110111': 8,
     '0001011': 9,
}
def find_pos(arr):
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == 1:
                return i,j-55
t= int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input())) for _ in range(n)]

    sx, sy = find_pos(arr)

    pwd = [] # 암호코드
    for _ in range(8):
        pwd.append(mapping.get(''.join(map(str,arr[sx][sy:sy+7]))))
        sy += 7
    # 검증
    odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
    even = pwd[1] + pwd[3] + pwd[5] + pwd[7]

    if (odd *3 + even) % 10 == 0:
        print(f'#{tc} {sum(pwd)}')
    else:
        print(f'#{tc} 0')