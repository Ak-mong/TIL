person = {
    'name':'Alice',
    'age':25
    }

# print(person['name'])
# print('get():',person.get('name')) #Alice
# print(person.get('country')) #None
# print(person.get('country', '키가없습니다.')) #Unkown

# print(person.keys()) #dict_keys(['name', 'age'])
# # person.clear()
# for key in person.keys():
#     print(key)
# print(person)

# print(person.values())
# for v in person.values():
#     print(v)

# print(person.items())
# for key,value in person.items():
#     print(key,value)

# print(person.pop('age'))
# print(person)
# print(person.pop('country',None))

print(person.setdefault('country','KOREA'))
print(person) #{'name': 'Alice', 'country': 'KOREA'}

other_person = {
    'name' : 'Jane',
    'gender':'Female'
}
person.update(other_person)
print(person)

person.update(age=50, country = 'USA')
print(person)

list = [
    {'john' : '521-1234'},
    {'Lisa' : '521-8976'},
    {'Sandra' : '521-9655'},
]
dict = {
    'john' : '521-1234',
    'Lisa' : '521-8976',
    'Sandra' : '521-9655'
}

dict.get('Lisa')