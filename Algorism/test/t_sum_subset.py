import sys; sys.stdin = open('../txt/sum_subset.txt')
t= int(input())
arr = list(range(1,13))
N = len(arr)
for tc in range(1,t+1):
    n,k = map(int,input().split())

    ans = 0
    for i in range(1,1<<n):
        sum, cnt = 0, 0
        for j in range(len(arr)):
            if i & (1<<j):
                sum += arr[j]
                cnt += 1
                print((i,j),1<<j)

        if sum == k and cnt == n:
            ans += 1
    print(f'#{tc} {ans}')
    # print(list(range(1,1<<n)))
    # print(list(range(1<<len(arr))))

"""
print('1-------')
print(1<<1) # 1*2
print(1<<2) # 1*2*2
print(1<<3) # 1*2*2*2
print(1<<4) # 1*2*2*2*2
print('2------')
print(2<<1)
print(2<<2)
print(2<<3)
print(2<<4) #1110
print('3--------')
print(3<<1) # 3*2
print(3<<2) # 3*2*2
print(3<<3) # 3*2*2*2
print(3<<4) # 3*2*2*2*2
"""