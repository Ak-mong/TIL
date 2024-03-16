t = int(input())

def find_GCD(a,b):
    r = a%b
    if r == 0:
        return b
    else:
        return find_GCD(b,r)

for _ in range(t):
    arr = list(map(int,input().split()))
    n = arr[0]
    num_arr = arr[1:]
    sum_v = 0
    for i in range(n-1): # n-1 과 n 번째 인덱스를 비교해야되기 때문
        for j in range(i+1,n):
            sum_v += find_GCD(num_arr[i],num_arr[j])
    print(sum_v)