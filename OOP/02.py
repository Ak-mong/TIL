class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()

p2 = Person()
p2.name = 'kim'
p2.talk()

print(Person.name)
print(p1.name)
print(p2.name)
p3 = Person()

p2.ssafy = 11 # 없는 변수 추가 가능
print(p2.ssafy)
print(p2.ssafy)
print(p2.name)
