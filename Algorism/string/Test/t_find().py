def my_find(t,p):
    for i in range(len(t)-len(p)+1):
        flag = 1
        for j in range(len(p)): #패턴 돌리기
            if t[i+j]!= p[j]:
                flag = 0
                break
        if flag: # true면
            return i
    return -1
text = 'ABDABCD'
patten = 'ABC'

# print(text.find(patten))
# print(patten in text)
print(my_find(text,patten))