
def capitalize_words(text):
    lst = text.split()
    cap_lst = []
    for i in lst:
        i = i.capitalize()
        cap_lst.append(i)
    return ' '.join(cap_lst)
    pass






result = capitalize_words("hello, world!")
print(result)