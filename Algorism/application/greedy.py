'''
화장실 문제

'''
arr = [15,30,50,10]
arr.sort()
sum = 0
for i in range(len(arr)):
    sum +=arr[i] * (len(arr)-1-i)

print(sum)

