# 아래 함수를 수정하시오.
def get_keys_from_dict(input_dict):
    return list(input_dict.keys())

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

def get_keys_from_dict2(input_dict):
    key_list = []
    value_list = []
    for key in input_dict:
        key_list.append(key)
        value_list.append(input_dict[key])
    return key_list, value_list
my_dict = {'name': 'Alice', 'age': 25}
result2 = get_keys_from_dict2(my_dict)
print(result2)  # ['name', 'age']
