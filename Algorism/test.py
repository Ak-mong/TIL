import sys;
sys.stdin =open('input.txt')

s = int(input())
sum_v = 0
cnt = 0
i = 0
while sum_v <= s:
    i += 1
    cnt += 1
    sum_v += i


# print(i)
if s - sum_v <= i:
    sum_v -= i
    sum_v -= i-1
    cnt -= 2
    cnt += 1
else:
    sum_v -= i
    cnt -= 1

print(cnt)
# print(sum_v)
