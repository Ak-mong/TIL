<<<<<<< HEAD
# import sys
# sys.stdin = open("txt/list_sum.txt", "r")

def print_hi(name):
    # t = int(input())  # 상자가 쌓여있는 가로 길이
    #
    # for tc in range(t):
    #     n, m = map(int, input().split())  # 상자가 쌓여있는 가로 길이
    #
    #     numbers = list(map(int, input().split()))
    #     lst = [sum(numbers[:m])]
    #     for i in range(1, n - m + 1):
    #         _sum = lst[i - 1] - numbers[i - 1] + numbers[i + m - 1]
    #         lst.append(_sum)
    #
    #     print(f'#{tc + 1} {max(lst) - min(lst)}')
    arr = [list(map(int, input())) for _ in range(10)]
    print(arr)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
=======
import sys
sys.stdin = open("txt/flatten", "r")

for tc in range(1, 11):
    dump_cnt = int(input())
    floor_list = list(map(int, input().split()))

    for _ in range(dump_cnt):
        max_index = 0
        min_index = 0

        for num in range(len(floor_list)):
            if floor_list[max_index] < floor_list[num]:
                max_index = num
            if floor_list[min_index] > floor_list[num]:
                min_index = num

        floor_list[max_index] -= 1
        floor_list[min_index] += 1

    for num in range(len(floor_list)):
        if floor_list[max_index] < floor_list[num]:
            max_index = num
        if floor_list[min_index] > floor_list[num]:
            min_index = num

    print(f"#{tc} {floor_list[max_index] - floor_list[min_index]}")
>>>>>>> 63926bd51f7baf780c7d3571454df1c1ad137f61
