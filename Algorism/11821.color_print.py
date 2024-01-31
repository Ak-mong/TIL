import sys , pprint
sys.stdin = open("txt/color_print.txt","r")
t = int(input())
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = [[0] * 10 for _ in range(10)]
# [r1, c1, r2, c2, color]
print(arr)
for tc in range(1,t+1):
    count = 0
    for a in range(len(arr)):
        r1 = arr[a][0]
        c1 = arr[a][1]
        r2 = arr[a][2]
        c2 = arr[a][3]
        color = arr[a][4]
        for i in range(r1, r2+1):
            for j in range(c1,c2+1):
                # if color != arr[a-1][4]:
                cnt[i][j] += 1
                    # if cnt[i][j] == 2:
                    #     count +=1
    # pprint.pprint(count)
    # pprint.pprint(cnt)
# print(r1, c1, r2, c2, color)


