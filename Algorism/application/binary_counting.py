friends = ['a','b','c','d','e']
n = 5
m = 2
# 5P2
def getFriend(tar):
    cnt = 0
    for i in range(n):
        # 1비트 1인지 확인
        if tar & 0x1:
            # print(friends[i], end='')
            cnt += 1
        # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
        tar >>= 1
    return cnt
# getFriend(m)
result = 0
for j in range(1<<n):
    if getFriend(j) >= 2: # bit가 2개이상 1이라면 -> 2명 이상이라면?
        result += 1
print(result)