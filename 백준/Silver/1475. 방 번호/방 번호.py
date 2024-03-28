# 1475 방번호 실버 5
n = input()
arr = [0] * 10
for i in n:
    i = int(i)
    arr[i] += 1
if arr[6] < arr[9]:
    arr[9] = (arr[6] + arr[9] + 1) // 2
else:
    arr[6] = (arr[6] + arr[9] + 1) // 2
print(max(arr))
