class Circle():
    pi = 3.14
    def __init__(self,r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

# c2 인스턴스 변수 pi를 할당
c2.pi = 5
print(Circle.pi)
print(c1.pi)
print(c2.pi)