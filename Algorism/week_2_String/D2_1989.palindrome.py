import sys; sys.stdin = open('txt/palindrome')
t = int(input())
for tc in range(1,t+1):
    a = input()
    flag = 1
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            flag = 0
    print(f'#{tc} {flag}')
