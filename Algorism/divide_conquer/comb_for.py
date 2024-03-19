# 순열 : 뽑고 줄세우기
# 조합 : 뽑기
# 중복 순열 > 순열 > 중복조합 > 조합

# 반복 조합 5C3
arr = [1,2,3,4,5]
n = len(arr)

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            print(arr[i],arr[j],arr[k])


