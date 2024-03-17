# 1026 보물 실4
n = int(input())
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))

arr_a.sort()
sum_v = 0
i = 0
while arr_b:
    sum_v += max(arr_b) * arr_a[i]
    arr_b.remove(max(arr_b))
    i += 1

print(sum_v)