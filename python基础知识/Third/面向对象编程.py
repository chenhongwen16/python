'''
类就是一系列对象相似的特征与技能的结合体
在现实世界中：先有对象再有类
在程序中：先有类再有对象，一定先定一类，后调用类来产生对象


'''

class LuffyStudent:
    school = 'luffycity'
    def learn(self):
        print('is learning')
    def eat(self):
        print('is eating')
    def sleep(self):
        print('is sleeping')

#后产生对象

stu1 = LuffyStudent()
stu2 = LuffyStudent()
stu3 = LuffyStudent()

print(stu1)
print(stu2)
print(stu3)