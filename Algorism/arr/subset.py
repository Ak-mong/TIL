N = 5
arr = [1,2,3,4,5]
# arr = [3,6,7,1,5,4]
# n = len(arr) #n:원소의 개수
for i in range(1<<N): #2의 n제곱 -1 까지(range()니까)
    s = 0
    for j in range(N):
        if i & (i<<j):
            s += arr[j]
            print(arr[j], end=' ')
    print()