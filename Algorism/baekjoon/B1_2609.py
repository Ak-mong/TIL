import sys;sys.stdin=open('input.txt')

n1, n2 = map(int,input().split())

i = 2
arr = []
while i < 10000:
    while n1%i==0 and n2%i==0:
        n1 //=i
        n2 //=i
        arr.append(i)
    i += 1
arr.append(n1)
arr.append(n2)
# print(arr)
sum_v = 1
for i in range(len(arr)-2):
    sum_v *= arr[i]
print(sum_v)
sum_v *= arr[-1] * arr[-2]
print(sum_v)
