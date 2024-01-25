# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self, sound):
        self.sound = sound
        return self.sound

class Cat(Animal):

    def __init__(self,sound):
        super().__init__(sound)

    def meow(self):
        return print(self.sound)

cat1 = Cat("야옹!")
cat1.meow()
