class MyClass:
    def instance_method(self):
        print("This is an instance method")
obj = MyClass()
obj.instance_method()

class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")
MyClass.class_method()

class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")
MyClass.static_method()
