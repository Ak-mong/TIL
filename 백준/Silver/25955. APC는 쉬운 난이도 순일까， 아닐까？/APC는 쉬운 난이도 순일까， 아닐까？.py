import sys
input = sys.stdin.readline

# 25955 APC는 쉬운 난이도 순일까, 아닐까?
n = int(input())
arr = input().split()
data = {
   'B':0,
   'S':1,
   'G':2,
   'P':3,
   'D':4,
}
path = []
arr2, x = [0]*n, []
for i in range(n):
    arr2[i] = data[arr[i][0]]*1000+(1000-int(arr[i][1:]))
sort_arr = sorted(arr2)
if arr2 == sort_arr: print('OK')
else:
    print('KO')
    for i in range(n):
        if arr2[i] != sort_arr[i]:
            path.append(arr[i])
    print(*reversed(path))
