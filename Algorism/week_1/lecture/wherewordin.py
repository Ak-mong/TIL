k = 3
n = 6
arr= [0,1,0,1,1,1]
"""
두 번째 방법
n = 7
arr= [0,1,0,1,1,1,0]
"""

ans = 0
cnt = 0
for i in range(n):
    if arr[i] == 0: # 0이라면
        if cnt == k:
            ans += 1
        cnt = 0
    else: #arr[i] == 1
        cnt += 1
        # arr 뒤에 0을 붙이면 하단 코드는 없어도 된다.
        if i ==n-1: # and cnt ==k 로 바꿔도 된다. 이중 if문 이기 때문에 and 쓰면 짧아짐
            if cnt == k:
                ans += 1
print(ans)
