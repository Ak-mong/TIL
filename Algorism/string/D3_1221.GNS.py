import sys; sys.stdin = open('txt/GNS.txt')
t = int(input())
for tc in range(1,t+1):
    n = int(input().strip(' ')[-4:])
    arr = list(map(str,input().split()))
    num_dict = {}
    count = [0] *10
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # temp = arr[:] #1차원이니까 얕은복사로 충분
    temp = []
    for i in range(len(num_list)):
        num_dict.setdefault(num_list[i],i)
    for i in arr:
        count[num_dict[i]] += 1
    for i in num_dict:
        for j in range(count[num_dict[i]]):
            temp.append(i)
    # str_temp = ' '.join(temp)
    print(f'#{tc}')
    # print(str_temp)
    print(*temp)