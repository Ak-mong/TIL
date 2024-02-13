import sys;sys.stdin = open('../txt/string4.txt')
t = int(input())
for tc in range(1, t + 1):
    str1 = input()
    str2 = input()
    # set 을 이용한 중복 제거
    # str1 = list(set(str1))
    # dict 을 이용한 중복 제거
    my_dict = {}
    for key in str1:
        my_dict[key] = 0
    # 카운팅
    for key in str2:
        if my_dict.get(key) != None:
            my_dict[key] += 1
    # 최대값
    ans = 0
    for v in my_dict.values():
        if ans < v: ans = v

    print(f'#{tc} {ans}')
