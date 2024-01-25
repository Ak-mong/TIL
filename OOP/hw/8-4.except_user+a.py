class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            self.name = input('이름을 입력하세요 : ')
            self.age = input('나이을 입력하세요 : ')
            self.user_data[self.name] = int(self.age)
            return self.name, int(self.age)
        except (ValueError):
            if self.age.isalpha():
                if not self.age.isdigit() :
                    print('나이는 숫자로 입력해야 합니다.')  
                    pass

    def display_user_info(self):
        if self.age.isdigit():
            if self.user_data != {}:
                print('사용자 정보:')
                print('이름 : ', self.name)
                print('나이 : ', self.age)             
            else:
                try:
                    print('사용자 정보가 입력되지 않았습니다.')
                except:
                    pass
        else:
            if self.user_data == {} and self.age =='':
                print('사용자 정보가 입력되지 않았습니다.')
            else:
                pass
            
user = UserInfo()
user.get_user_info()
user.display_user_info()