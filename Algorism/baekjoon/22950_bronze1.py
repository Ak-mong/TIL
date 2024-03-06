import sys; sys.stdin = open('input.txt')
# input = sys.stdin.readline
# 22950 이진수 나눗셈 브론즈1
'''
충분히 큰 수 + 시간제한
=> 시간복잡도를 생각해야한다.
'''
n = int(input())
m = input()
k = int(input())
if '1' not in m:
    print('YES')
    exit(0)
if k==0:
    print('YES')
    exit(0)
# count = 0
# for i in range(len(m)-1,-1,-1):
#     if m[i] == '1': break
#     if m[i] == '0': count +=1
#
# if count >= k: print('YES')
# else: print('NO')
# if int(m) == 0:
#     print('YES')
#     exit(0)
x = -1
cnt = 0
while m[x] == '0':
    x -= 1
    cnt += 1
    if cnt ==n:
        break
# print(cnt)
if cnt >= k:
    print('YES')
else:
    print('NO')


