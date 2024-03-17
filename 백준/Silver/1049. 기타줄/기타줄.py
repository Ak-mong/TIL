# 1049 기타줄 실버4
n, m  = map(int,input().split())
arr_6 = []
arr_1 = []
for _ in range(m):
    x,y = map(int,input().split())
    arr_6.append(x) # 6개짜리
    arr_1.append(y) # 1개 짜리
# print(arr_6      ,arr_1)
arr_6.sort()
arr_1.sort()
sum_v = 0
if arr_6[0] >= arr_1[0] * 6:
    sum_v = n * arr_1[0]
elif arr_6[0] >= (n % 6) * arr_1[0]:
    sum_v = (n//6) * arr_6[0] + (n % 6) * arr_1[0]
else:
    sum_v = (n//6 +1) * arr_6[0]
print(sum_v)