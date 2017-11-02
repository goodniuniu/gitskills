class Person:
     # "Person类"
    def __init__(self, name, age, gender):

        print('进入Person的初始化')
        self.name = name
        self.age = age
        self.gender = gender
        print('离开Person的初始化')

    def getName(self):
        print(self.name)
P1 = Person('ice', 18, '男')
