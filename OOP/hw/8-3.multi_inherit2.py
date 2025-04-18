# 확인용 예시
# 새로운 모델 인스턴스 생성
class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
    
class Other(BaseModel):
    TYPE = 'Other Model'
    def save(self):
        print('데이터를 다른 장소에 저장합니다.')
    
class ExtendedModel(Novel, Other):
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at,author)
        self.extended_type = extended_type

    def display_info(self):
        print(f'PK: {self.PK}')
        print(f'TYPE: {self.TYPE}')
        print(f'EXTEBDED_TYPE: {self.extended_type}')

    def save(self):
        print('데이터를 확장해서 저장합니다.')
    pass

extended_instance = ExtendedModel('확장', '확장 모델', '모델 내용', 2022, 2024, '확장 작가', 'Extended Type')

# 새로운 모델의 메서드 호출
print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
extended_instance.display_info()
extended_instance.save()