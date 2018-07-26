class People:
    def walk(self):
        print('is walking')
class Pig:
    def run(self):
        print('is running')
class Dog:
    def zou(self):
        print('is zouing')


peo1 = People()
pig1 = Pig()
dog1 = Dog()

peo1.walk()
pig1.run()
dog1.zou()


'''
通过抽象类，定义接口
抽象类不能被实例化

import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass
        
        
    @abc.abstractmethod
    def eat(self):
        pass   

'''