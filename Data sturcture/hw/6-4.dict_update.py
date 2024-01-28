# 아래 함수를 수정하시오.
def add_item_to_dict(input_dict, key ,value):
    new_dict = input_dict.copy()
    new_dict.update({key:value})
    # 없으면 추가, 있으면 수정
    new_dict[key] = value
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

def add_item_to_dict2(input_dict, key ,value):
    # new_dict = input_dict
    input_dict.setdefault(key,value)
    return input_dict


result2 = add_item_to_dict2(my_dict, 'country', 'USA')
print(result2)