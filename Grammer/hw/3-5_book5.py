number_of_people = 0
number_of_book = 100
many_user = None

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    print(f'{name[number_of_people]}님 환영합니다!')
    number_of_people += 1
    return number_of_people

def create_user(name, age, address):
    increase_user()
    return {'name':name, 'age':age, 'address':address}

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')
    return number_of_book
    
many_user = list(map(create_user,name, age, address))
info = list(map(lambda x : {'name': x['name'], 'age':x['age']//10}, many_user))

def rental_book(info):
    pass
    decrease_book(info['age'])
    return print( f"{info['name']}님이 {info['age']}권의 책을 대여하였습니다.")
    
list(map(rental_book, info))