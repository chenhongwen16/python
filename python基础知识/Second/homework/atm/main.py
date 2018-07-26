'''
__author__:evan
'''
import os
import sys
from core import shopping

msg = '''
        =========业务列表=======
        1.购物商城
        2.信用卡中心
        3.日志查询
        4.后台控制
        '''
print(msg)

while True:
    choice = input('please input your choice:')
    choice = int(choice)
    if choice == 1:
        shopping.shopping()
    elif choice == 2:
        pass



