# def restructure_word(word, arr):
#     arr.extend(original_word)
#     print(arr)
#     for i in word:
#         if i.isdecimal():
#             for j in range(int(i)):
#                 arr.pop()
#         else:
#             arr.remove(i)
#     return arr

# original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# arr = []

# result = restructure_word(word, arr)
# print(result)
# print("".join(result))

# print('-'*30)
# print('강사님 코드')
# def restructure_word2(word,arr2):
#     for ch in word:
#         if ch.isdecimal():
#             for _ in range(int(ch)):
#                 arr2.pop()
#         else:
#             arr2.remove(ch)
#     return arr2

# arr2 = []
# for ch in original_word:
#     arr2.extend([ch])
# print(arr2)

# result2 = restructure_word2(word,arr2)
# print(result2)
# print(''.join(result2))

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
for i in original_word:
    arr.extend([i])
print(arr)
def restructure_word(word, arr):
    for i in word:
        if i.isdecimal():
            for _ in range(int(i)):
                arr.pop()
        else:
            arr.remove(i)
    return arr
result = restructure_word(word, arr)
print(result)
print(''.join(result))