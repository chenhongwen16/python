class LuffyStudent:
    school = 'luffycity'#数据属性
    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age

    def learn(self):#函数属性
        print('is learning')

    def eat(self):
        print('is eating')





stu1 = LuffyStudent('wan','女',18)

print(stu1.Age)

#实例化的步骤，__init_
#1 先产生一个控对象
#2 LuffyStudent.__init__(stu1,'wan','女',18)

