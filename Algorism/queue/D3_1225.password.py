import sys;sys.stdin = open('txt/password.txt')
def password():
    front = rear = -1
    while True:
        if arr[rear % N] > 0:
            for i in range(N):
                for j in range(1, 6):
                    rear += 1
                    a = arr.pop(0) - j
                    if a <= 0:
                        a = 0
                        arr.append(a)
                        return
                    arr.append(a)
        else:
            break
for i in range(10):
    tc = int(input())
    N = 8
    arr = list(map(int,input().split()))
    password()
    print(f'#{tc}',*arr)