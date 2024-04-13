import sys
input = sys.stdin.readline
# 4153직각 삼각형 브3
while True:
    arr = list(map(int,input().split()))
    # if a ==0 and b ==0 and c ==0:
    #     break
    if max(arr) ==0: break
    arr.sort()
    if (arr[0]**2 + arr[1] ** 2)**(1/2) == arr[2]:
        print('right')
    else:
        print('wrong')