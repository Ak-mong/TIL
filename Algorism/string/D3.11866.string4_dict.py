import sys;sys.stdin = open('txt/string4.txt')
t = int(input())
for tc in range(1,t+1):
    # 원형
    patten = list(input())
    text = list(input())
    n = len(patten)
    m = len(text)
    text_dict = {}
    for i in patten:
        text_dict[i] = 0
    for j in text:
        if j in text_dict:
            text_dict[j] += 1
    max_v = 0
    for k in text_dict:
        if max_v < text_dict[k]:
            max_v = text_dict[k]
    # print(text_dict)
    print(f'#{tc} {max_v}')