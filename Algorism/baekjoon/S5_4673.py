'''
n + n//10 + n%10

str(n)//10**i
'''
def d(n):
    sum_v = n
    for j in range(len(str(n))):
        sum_v += n%10
        n //= 10
    # print(n + sum_v)
    new_arr.append(sum_v)

# str(1000)
n = 10000
# new_arr= [2,4,6,8,10,12,14,16,18]
new_arr=[]
for i in range(1,n+1):
    d(i)
# d(9971)
arr = [_ for _ in range(1,n+1)]
# print(new_arr)
for x in arr:
    if x not in new_arr:
        print(x)
