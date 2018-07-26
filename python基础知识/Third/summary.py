#属性查找小练习
'''
先从对象的本身去找，然后从对象的类，再然后是类的父类
'''



'''
多继承的时候 
属性查找怎么找


1.子类会优先父类被检查
2.多个父类会根据他们再列表中的顺序被检查
3.如果对下一个类存在两个合法的选择，选择第一个父类

列表的顺序按照什么顺序排

深度优先
广度优先


继承是实现原理

1、新式类
2、经典类

只在python2中分 python3中全是新式类

在python2中-》》经典类：没有继承object的类
新式类：继承了object类，以及他的子类都称之为新式类



'''
class Foo:
    pass
class Bar(Foo):
    pass


class Foo(object):
    pass
class Bar(Foo):
    pass
'''
在python3中——》》新式类,一个类没有继承object类，默认就继承了object类
'''

class Foo:
    pass
print(Foo.__bases__)

'''
chenhongwendeMacBook-Pro:Third chenhongwen$ python3 summary.py 
(<class 'object'>,)

经典类 深度优先
新式类 广度优先
.mro()


自己试一下
'''


'''
在子类中重用父类的属性
'''