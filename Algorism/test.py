N = int(input())
i = 2
while N != 1: # 나누어 떨어지는 동안
    if N % i != 0:
        i +=1
    else:
        N /= i # i로 나눈다
        print(i)


