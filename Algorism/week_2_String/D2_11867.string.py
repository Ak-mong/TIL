import sys;sys.stdin = open('txt/string')

t = int(input())
def f_find(text,patten):
    for i in range(len(text)-len(patten)+1):
        flag = 1
        for j in range(len(patten)):
            if text[i+j] != patten[j]:
                flag = 0
                break
        if flag:
            return 1
    return 0
for tc in range(1,t+1):
    str1 = input()
    str2 = input()
    result = f_find(str2,str1)
    print(f'#{tc} {result}')