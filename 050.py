class MyClass:
    var = '안녕하세요!!'
    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()
#obj.param1