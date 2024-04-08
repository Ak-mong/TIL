import sys
input=sys.stdin.readline
n, m = map(int,input().split())
# 1 <=  N,m <= 100000
# 도감 번호와 이름이 연결되있어야 한다
pokmon_dict1 = {}
pokmon_dict2 = {}
for i in range(n):
    name = input().strip()
    pokmon_dict1[name] = i+1
    pokmon_dict2[i+1] = name
for i in range(m):
    find_pkmon = input().strip()
    if find_pkmon.isdigit():
        print(pokmon_dict2[int(find_pkmon)])
    else:
        print(pokmon_dict1[find_pkmon])