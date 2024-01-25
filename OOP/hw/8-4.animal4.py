# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self, meow):
        self.meow = meow
        return self.meow

class Cat(Animal):

    def __init__(self,meow):
        super().__init__(meow)

    def meow(self):
        return print(self.meow)
class Dog(Animal):
    def __init__(self,meow):
        super().__init__(meow)

    def bark(self):
        return print(self.meow)

    pass
class Pet(Dog,Cat):
    def __init__(self,meow,sound):
        super().__init__(meow)
        self.sound = sound
    def play(self):
        return '애완동물과 놀기'
    def make_sound(self):
        return self.sound
    pass


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
