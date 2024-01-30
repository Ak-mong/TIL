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
