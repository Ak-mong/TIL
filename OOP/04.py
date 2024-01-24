class MyClass:
    def instace_method():

    @classmethod
    def class_method():
        return 'static method'
    @staticmethod
    def static_method():
        return 'static method'
    
# 클래스가 전부 다 호출해보기
instance = MyClass()
print(MyClass.instance_method(instance))
print(MyClass.class_method(instance))
print(MyClass.static_method(instance))

# 클래스가 전부 다 호출해보기
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())
