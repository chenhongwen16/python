# class Foo:
#
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def A(cls):
#         print(cls)
#
#     @staticmethod
#     def sum(x,y):
#         print(x+y)

'''
绑定方法能够自动传值
非绑定方法不能自动传值
'''

class People:
    def __index__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):#绑定到对象的方法
        print('Name:%s Age:%s Sex:%s'%(self.name,self.age,self.sex))


