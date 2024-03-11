import sys; sys.stdin= open('input.txt')
a,b,v = map(int,input().split())
# v미터 나무에 낮에 a미터 올라감 밤에 b만큼 내려감, 모두올라갈때 며칠걸리냐
# 2 -1 2 -1 2-1 2 -1 2
# sum_v = 0
# day = 0
# while sum_v < v:
#     sum_v += a
#     day += 1
#     if sum_v >= v:
#         break
#     sum_v -= b
# while True:
#     result = v-a
#     result -= (a+b)
#     day += 1
#     if result <= 0:
#         break
# print(result)
if (v-b) % (a-b) == 0: # 딱떨어진다면
    print((v-b) // (a-b) )
else:
    print((v-b ) // (a - b) + 1)

# print(day+1)