class Person:
    # 속성
    blood_color = 'red'
    age = 10
    count = 0
    #생성자 함수
    def __init__(self, name): # 이건 인스턴스가 못씀, name은 인스터스가 가지는 변수
        # 인스턴스 변수
        self.name = name
        self.age = name
        Person.count += 1
        pass
    
    # 인스턴스 메서드
    def singing(self):
        # Person.age += 1 # 비추 하는 방법
        return f'{self.name}가 노래합니다.'
    def aging(self):
        return f'{self.age}'
    
    # 클래스 메서드
    @classmethod
    def number_of_populations(cls):
        print(f'인구수는 {cls.count}입니다.')
    
    #스태틱 메서드
    @staticmethod
    def greeting():
        print('안녕하세요')
# 인스턴스 생성
singer1 = Person('iu')
singer2 = Person('BTS')
aging1 = Person(50)

# 메서드를 호출
print(singer1.singing())
print(singer2.singing())
# 설계도는 다른데, 결과는 다르다.

print(singer1.blood_color)
print(singer2.blood_color)

print(Person.age)
print(aging1.aging())
singer2.age = 30
print(singer2.age)


Person.number_of_populations() #인스턴스 생성한 갯수
Person.greeting()