# 1193 분수 찾기 실버5
num = int(input())
line = 1
while num > line:
    num -= line
    line += 1
# print(line)
if line %2: # 라인이 홀수 라면
    a = line -num + 1
    b = num
else:
    a = num
    b = line -num + 1
print(f'{a}/{b}')