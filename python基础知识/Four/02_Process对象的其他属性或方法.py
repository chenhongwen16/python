# join方法
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
#     p.join()
#     print('zhu')

# from multiprocessing import Process
# import time
# def task(name,n):
#     print('%s is running ' %name)
#     time.sleep(n)
#     print('%s is done' %name)
#
# if __name__ == '__main__':
#     start = time.time()
#     p1 = Process(target=task, args=('子进程1',5))
#     p2 = Process(target=task, args=('子进程2',3))
#     p3 = Process(target=task, args=('子进程3',2))
#
#     p1.start()  #仅仅只是给操作系统发送了一个信号
#     p2.start()
#     p3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     print('zhu', (time.time()-start))

from multiprocessing import Process
import time
def task(name,n):
    print('%s is running ' %name)
    time.sleep(n)
    print('%s is done' %name)

if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=('子进程1',5))
    p2 = Process(target=task, args=('子进程2',3))
    p3 = Process(target=task, args=('子进程3',2))

    p1.start()  #仅仅只是给操作系统发送了一个信号
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
    print('zhu', (time.time()-start))


#p.is_alive()看进程是否活着
#p.terminate()  干死进程 但是不会立即回收内存
#p.name


#内存隔离

