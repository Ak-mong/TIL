n,k = map(int,input().split())
prime = [1] * (n+1)
cnt = 0
for i in range(2,n+1):
    if prime[i]:
        for j in range(i,n+1,i):
            if prime[j]:
                cnt += 1
                prime[j] = 0
                # print(j)
                if cnt == k:
                    print(j)
                    exit(0)