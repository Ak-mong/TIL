# 1316 그룹 단어 체커 실버5

'''
한개짜리 단어도 ok
같은 문자열이 이어져야된다

'''
def check_word(word):
    global result
    dicts = {}
    cnt = 0
    for i in range(len(word)):
        if dicts.get(word[i]): # 딕셔너리 값이 있따면
            dicts[word[i]] += 1
        else: # 값이 없다면
            dicts[word[i]] = 1
    for j in range(len(word)-1):
        # 전 인덱스와 비교해서 다를 때
        if word[j] != word[j+1]:
            # 현재 개수가 cnt와 다르다면 cnt = 1 로 만든다
            if cnt+1 != dicts.get(word[j]): return
            cnt = 0
        else:
            cnt += 1
    result += 1


n = int(input())
result = 0
for _ in range(n):
    word = input()
    check_word(word)
print(result)