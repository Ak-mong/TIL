name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    return {'name':name, 'age':age, 'address':address}

print(list(map(create_user,name, age, address)))
# create_user()

