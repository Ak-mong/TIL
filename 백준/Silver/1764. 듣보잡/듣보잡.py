import sys
input = sys.stdin.readline

# 1764 듣보잡 실버4
n,m = map(int,input().split())
n_arr = set()
m_arr = set()
for _ in range(n):
    n_arr.add(input().strip())
for _ in range(m):
    m_arr.add(input().strip())
result = n_arr & m_arr
print(len(result))
for j in sorted(result):
    print(j)