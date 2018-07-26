#/usr/bin/env python3
#coding:utf-8

import os

def search():
    print('''
    查询试列
    find * from per_info where age > 22
    find * from per_info where dept = "IT"
    find * from per_info where enroll_date like "2013"
    ''')
    select = input("please input what you want to search >>>")
    select = select.strip().split()
    con = select[7]
    asp = select[5]
    count = 0
    with open('./per_info.txt','r') as f:
        '''
        for line in f.readline()为什么会报错
        '''
        if asp == 'age':
            for line in f:
                if int(line.strip().split(',')[2]) > int(con):
                    print(line)
                    count += 1
        elif asp == 'dept':
            for line in f:
                if line.strip().split(',')[4] in con :
                    print (line)
                    count += 1
        else:
            for line in f:
                if line.split(',')[5].split('-')[0] in con:
                    print (line)
                    count += 1
        print('查到信息 %d 条'%count)


def add():
    print('''
        添加试列
        name,age,phone,dept,enroll-date
        ''')
    in_put = input('please input what you want to add >>>')
    in_put = in_put.strip().split(',')
    phoneid = in_put[2]
    list_all = []
    f = open('./per_info.txt','r+')
    for line in f:
        list_all.append(line.strip().split(',')[3])
    if phoneid in list_all:
        print ("已经存在相同的phoneid,添加失败")
        f.close()
    else:
        for line in f:
            f.write(line)
        staff_id = str(len(list_all) + 1)
        in_put.insert(0, str(staff_id))
        f.write('\n')
        f.write(','.join(in_put))
        f.close()
        print('Add successfully!')

def delete():
    print('''
            删除试列
            delet from per_info where staff_id = 12
            ''')
    delete_id = input('please input what you want to delete >>>')
    delete_id = delete_id.strip().split()[6]
    f = open('./per_info.txt','r')
    f_new = open('per_info.txt','w')

    for line in f:
        in_list = line.split(',')
        if in_list[0] < delete_id:
            f_new.write(line)
        elif in_list[0] > delete_id:
            in_list[0] = str(int(in_list[0])-1)
            f_new.write(','.join(in_list))
        else:
            continue
    f.close()
    f_new.close()
    os.remove('./per_info.txt')
    os.rename('./new_per_info.txt','./per_info.txt')
    print ('Deleted successfully!')

def change():
    print('''
            更新试列
            UPDATE per_info SET dept = HR where dept = 运维
            ''')
    data = input('please input what you want to update >>>')
    new = data.strip().split()[5]
    old = data.strip().split()[9]
    f = open('./per_info.txt', 'r')
    f1 = open('./new_per_info.txt', 'w')
    for line in f:
        if old in line:
            line = line.replace(old, new)
        f1.write(line)
    f.close()
    f1.close()
    os.remove('./per_info.txt')
    os.rename('./new_per_info.txt', './per_info.txt')
    print('Update successfully!')

def main():
    while True:
        print("""
       1:查询
       2:添加
       3:删除
       4:修改
       5:退出
       """)
        choice = input('输入序号：')
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                search()
            elif choice == 2:
                add()
            elif choice == 3:
                delete()
            elif choice == 4:
                change()
            elif choice == 5:
                exit()
            else:
                print ("please check your input num, it should be between 1 and 5")
        else:
            print ("Your input is illegally!")
if __name__ == '__main__':
    main()