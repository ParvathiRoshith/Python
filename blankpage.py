class Test:
    a = 10              #static variable
    def __init__(self,default_variable=999):
        self.b = 20     #instance variable
        self.p = default_variable
    def method1(self):
        c = 30          #local variable
        print(c)
    @classmethod
    def method2(cls):
        del Test.a      
        Test.x = 10
        cls.y = 10

t1=Test()
print(t1.__dict__)
print(t1.a)

t2=Test()
t2.method1()

t3 = Test()
t3.method2()
print(Test.y)