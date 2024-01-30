import sys
sys.stdin = open("txt/list_sum.txt", "r")

def print_hi(name):
    t = int(input())  # 상자가 쌓여있는 가로 길이

    for tc in range(t):
        n, m = map(int, input().split())  # 상자가 쌓여있는 가로 길이

        numbers = list(map(int, input().split()))
        lst = [sum(numbers[:m])]
        for i in range(1, n - m + 1):
            _sum = lst[i - 1] - numbers[i - 1] + numbers[i + m - 1]
            lst.append(_sum)

        print(f'#{tc + 1} {max(lst) - min(lst)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
