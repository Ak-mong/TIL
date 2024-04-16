import sys
input = sys.stdin.readline

# 1302 베스트셀러 실버4
n = int(input())
dicts = {}
for i in range(n):
    book = input().strip()
    dicts.setdefault(book)
    if dicts[book]:
        dicts[book] += 1
    else:
        dicts[book] = 1
result = []
for i in dicts.keys():
    if dicts[i] >= max(dicts.values()):
        result.append(i)
result.sort()
print(result[0])