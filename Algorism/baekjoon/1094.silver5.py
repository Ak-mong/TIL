import sys;
sys.stdin =open('input.txt')
import time
# starttime = time.time()
# 1094 막대기 실버5

'''
64
32 16 8 4 2 1
지민이가 가지고 있는 막대의 길이를 모두 더한다. 
처음에는 64cm 막대 하나만 가지고 있다. 
이때, 합이 X보다 크다면, 아래와 같은 과정을 반복한다.
가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
만약, 위에서 자른 막대의 절반 중 하나를 버리고 
남아있는 막대의 길이의 합이 X보다 크거나 같다면, 
위에서 자른 막대의 절반 중 하나를 버린다.
이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다.
'''
stick = 64
stick_arr = []

x = int(input())
while stick > 0:
    stick_arr.append(stick)
    stick //= 2
    # stick_arr.append(stick)
i = 0
sum_v = 0
cnt = 0
while i<len(stick_arr):
    if stick_arr[i] > x:
        i += 1
    else:
        x -= stick_arr[i]
        cnt += 1

# print(stick_arr)
print(cnt)