class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            self.name = input('이름을 입력하세요 : ')
            self.age = int(input('나이을 입력하세요 : '))
            self.user_data[self.name] = self.age
            return self.name, self.age
        except (ValueError):
            print('나이는 숫자로 입력해야 합니다.')  
            pass

    def display_user_info(self):
        try:
            if self.age:
                print('사용자 정보:')
                print('이름 : ', self.name)
                print('나이 : ', self.age)             
        except:
            print('사용자 정보가 입력되지 않았습니다.')
            
user = UserInfo()
user.get_user_info()
user.display_user_info()