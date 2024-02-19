# import requests
# from pprint import pprint as print

# # 무작위 유저 정보 요청 경로
# dummy_data = []
# for i in range(1,11):
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
#     # API 요청
#     response = requests.get(API_URL)
#     # JSON -> dict 데이터 변환
#     parsed_data = response.json()
#     if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
#         dict_data = {
#             'company' : parsed_data['company']['name'],
#             'name' : parsed_data['name'],
#             'lat' : parsed_data['address']['geo']['lat'],
#             'lng' : parsed_data['address']['geo']['lng'],
#         }
#         dummy_data.append(dict_data)

# black_list = [
#     'Hoeger LLC',
#     'Keebler LLC',
#     'Yost and Sons',
#     'Johns Group',
#     'Romaguera-Crona',
# ]

# def create_user(user_list, black_list):
#     censored_user_list = {}
#     for user in user_list:
#         company = user['company']
#         name = user['name']
#         if censorship(company, black_list):
#             if company not in censored_user_list:
#                 censored_user_list[company] = []
#             censored_user_list[company].append(name)
#     return censored_user_list
# # print(create_user(censored_user_list)
# def censorship(company, black_list):
#     if company in black_list:
#         print(f"{company} 소속의 {name} 은/는 등록할 수 없습니다.")
#         return False
#     else:
#         print("이상 없습니다.")
#         return True

# censored_user_list = create_user(dummy_data, black_list)
# print(censored_user_list)

num = int(input())
score = list(map(int,input().split()))
max_score = max(score)
print(sum(score) / max_score * 100 / num)