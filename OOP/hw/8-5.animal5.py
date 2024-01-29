class Dog():
    sound = '멍멍'
    def __init__(self):
        pass

class Cat():
    sound = '야옹'
    def __init__(self):
        pass
    
class Pet(Cat,Dog):
    def __init__(self):
        super().__init__()

    @classmethod    
    def __str__(cls):
        return f'애완동물은 {super().sound} 소리를 냅니다.'  

pet1 = Pet()
print(pet1)