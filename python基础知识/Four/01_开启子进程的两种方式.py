#方式一
# from multiprocessing import Process
# import time
# def task(name):
#     print('%s is running ' %name)
#     time.sleep(5)
#     print('%s is done' %name)
#
# if __name__ == '__main__':
#
#     p=Process(target=task,args=('子进程1',))
#     p.start()  #仅仅只是给操作系统发送了一个信号
#
#     print('zhu')

#方式二

from multiprocessing import Process
import time,os

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('%s is running' %self.name)
        time.sleep(3)
        print('%s is done' %self.name)

if __name__ == '__main__':
    p=MyProcess('子进程')
    p.start()

    print('zhu')
