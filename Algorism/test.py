import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()
# 실버 5
# N,K = map(int,input().split())
#
# arr = [list(map(int,input().split())) for _ in range(N)]
# # arr.sort(key=lambda x : (x[1],x[2],x[3]),reverse=True)
# new_arr = []
# for i in arr:
#     sum_v = i[1] * 3 + i[2]* 2 + i[3]* 1
#     new_arr.append([i[0],sum_v])
# new_arr.sort(key=lambda x : x[1],reverse=True)
# # 같은 등수일 때 어떻게 표현할까
# cnt = 0
# cnt2 = 0
# for i in range(len(new_arr)):
#     if new_arr[i][1] != new_arr[i-1][1]:
#         cnt += 1
#     else:
#         cnt2 += 1
#     new_arr[i].append(cnt)
# for x in new_arr:
#     if x[0] == K:
#         print(x[2])
# # print(new_arr)
#
#
#
dicts = {'author':'fda', 'title':'fdafda'}
print(dicts['author'])