import sys
sys.stdin= open("input.txt")
n = int(input())
arr= list(map(int,input().split()))
byte_v = int(input())
cnt = 0
for i in arr:
    if i % byte_v == 0:
        cnt += i//byte_v
    else:
        cnt += i//byte_v + 1

print(cnt*byte_v)