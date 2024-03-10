# 브1
name = input()
cnt = [0] * 91
for i in name:
    cnt[ord(i.upper())] += 1
# print(cnt)
max_i = 0
max_v = 0
question_list = []
for k in range(len(cnt)):
    if cnt[k] == 0:
        continue
    if max_v < cnt[k]:
        max_i = k
        max_v = cnt[k]
    elif max_v == cnt[k] :
        question_list.append(max_v)
if question_list and max_v<=max(question_list):
    print('?')
else:
    print(chr(max_i))