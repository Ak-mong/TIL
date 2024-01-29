# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self, meow):
        self.meow = meow
        return self.meow

class Cat(Animal):

    def meow(self):
        return print(self.meow)
class Dog(Animal):
    def bark(self):
        return print(self.meow)

class Pet(Dog,Cat):
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        return '애완동물과 놀기'
    def make_sound(self):
        return self.sound


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
