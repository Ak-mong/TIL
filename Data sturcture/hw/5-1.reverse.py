# 아래 함수를 수정하시오.
def reverse_string(string):
    reverse_str = ''.join(list(reversed(string)))
    return reverse_str


def reverse_string2(word):
    lst = list(word)
    lst.reverse()
    return ''.join(lst)



def reverse_string3(word):
    return word[::-1]

def reverse_string4(word):
    size = len(word)
    lst = list(word)
    for i in range(size//2):
        lst[i],  lst[size-1-i] = lst[size-1-i],lst[i]    
    return ''.join(lst)

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
result2 = reverse_string2("Hello, World!")
print(result2)
result3 = reverse_string3("Hello, World!")
print(result3)
result4 = reverse_string4("Hello, World!")
print(result4)