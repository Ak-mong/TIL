import sys;

sys.stdin = open('input.txt')
'''
어떤 정수 A가 있으면 그 수를 A = a1 * a2 * a3 * a4 ... * an으로 했을 때
A' = a1 + a2 + a3 ... + an이 성립하면 
"A는 A'으로 변할 수 있다"라고 한다.
(ai는 정수) 만약 A'이 A"으로 변할 수 있으면 "A는 A"으로 변할 수 있다"라고 한다.

이때 A와 B가 주어지면 A는 B로 변할 수 있는지 판별하시오.

입력
두 정수 A, B(-231 ≤ A, B ≤ 231-1)가 주어진다.

출력
각각의 테스트 케이스마다 한 줄에 변할 수 있으면 yes, 아니면 no를 출력한다.
'''


# def find_prime(input_num):
#     if input_num <= 2:
#         return [input_num, ]
#     for idx in range(2, input_num):
#         if input_num % idx == 0:
#             ret_list = []
#             val_a = find_prime(idx)
#             val_b = find_prime(int(input_num / idx))
#             ret_list = val_a + val_b
#             return ret_list
#     return [input_num, ]


t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    # arr = []
    sum_v = 0
    # prime_arr = find_prime(a)
    i = 2
    while i**2 <= a:
        while a % i == 0:
            sum_v += i
            # arr.append(i)
            # if (a//i) >= i and (a//i) % i !=0:
            #     arr.append(a//i)
            a //= i
        i += 1
    if a>1:
        # arr.append(a)
        sum_v += a
    # print(sum_v)
    # print(arr)
    if sum_v == b:
        print('yes')
    else:
        print('no')
