def d(n):
    sum_v = n
    for j in range(len(str(n))):
        sum_v += n%10
        n //= 10
    new_arr.append(sum_v)
n = 10000
new_arr=[]
for i in range(1,n+1):
    d(i)
arr = [_ for _ in range(1,n+1)]
for x in arr:
    if x not in new_arr:
        print(x)