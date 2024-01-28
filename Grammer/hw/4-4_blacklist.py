import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
dummy_data = []
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        dict_data = {
            'company' : parsed_data['company']['name'],
            'name' : parsed_data['name'],
            'lat' : parsed_data['address']['geo']['lat'],
            'lng' : parsed_data['address']['geo']['lng'],
        }
        dummy_data.append(dict_data)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(data):
    censored_user_list = {}
    for i in data:
        # censored_user_list = {i['company']: [i['name']]}
        censored_user_list.setdefault(i['company'],[i['name']])
    return censored_user_list

def censorship(dicts):
    valid_company = {}
    for key, value in dicts.items():
        if key in black_list:
            print(f'{key} 소속의 {str(value)}은/는 등록할 수 없습니다.')
        else:
            print('이상없습니다.')
            valid_company.setdefault(key, value)
    return valid_company

censored_user_list = create_user(dummy_data)
valid_company_list = censorship(censored_user_list)
print(valid_company_list)