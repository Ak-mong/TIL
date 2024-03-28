# 2217 로프 실버4
# (값 * 값의 인덱스)가 가장 큰 값
n = int(input())
rope = []
for _ in range(n):
    w = int(input())
    rope.append(w)
# print(rope)
rope.sort(reverse=True)
max_v = 0
for i in range(n,0,-1):
    sum = i * rope[i-1]
    if max_v < sum:
        max_v = sum
print(max_v)