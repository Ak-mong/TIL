data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
data1_list = []
for num in data_1:
    if num.isupper() or num == ' ':
        data1_list.append(num)
data1_list_str = ''.join(data1_list)
print(data1_list_str, end='')
print()

for num in data_1:
    if num.isupper() or num == ' ':
        print(num, end='')
print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
for i in '내힘들다':
    arr.append(data_2.find(i))
print(arr)
sort_arr = sorted(arr)
print(sort_arr)
for i in sort_arr:
    print(data_2[i], end='')
print()
print('-'*10)
arr2 = []
for ch in '내힘들다':
    result = data_2.find(ch)
    if result != -1:
        arr2.append(result)
print(arr2)

arr2.sort()
print(arr2)
for i in arr2:
    print(data_2[i], end='')