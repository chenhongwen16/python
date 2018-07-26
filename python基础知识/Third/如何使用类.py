class LuffyStudent:
    school = 'luffycity'#数据属性

    def learn(self):#函数属性
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')

    print('======run=====')

# def func():
#     x = 1
#     print('==>')
#
# func()


#查看类的名称空间
print(LuffyStudent.school)
print(LuffyStudent.__dict__)
print(LuffyStudent.__dict__['school'])
print(LuffyStudent.__dict__['learn'])

LuffyStudent.school #就是到类的内部寻找相应的俄东西

#查看属性
print(LuffyStudent.school)
print(LuffyStudent.learn)

#增加
LuffyStudent.county = 'China'
print(LuffyStudent.__dict__)
print(LuffyStudent.county)

#删除
del LuffyStudent.county

#改

LuffyStudent.school = 'Luffycity'


print(LuffyStudent.school)

stu1 = LuffyStudent()
stu2 = LuffyStudent()

