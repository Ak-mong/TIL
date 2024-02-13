def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

def f(i,k): # i 현재위치, k 목효
    if i == k:
        print(brr)
        # return
    else:
        brr[i] = arr[i]
        # print(arr[i])
        f(i+1,k)

arr = [10,20,30]
n = len(arr)
brr = [0] * n
f(0 ,n)
# print(factorial(5))