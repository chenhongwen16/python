#提交任务的两种方式
#同步调用



#异步调用
from concurrent.futures import ThreadPoolExecutor
import time, random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(2, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weight(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 <%s>kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)
    pool.submit(la, 'chw').add_done_callback(weight)
    pool.submit(la, 'zch').add_done_callback(weight)