#/usr/local/bin/env python3
#coding:utf-8

dic = {
    '成都':{'武侯':['四川大学','四川音乐学院'],
          '高新':['金融城','世纪城'],
          '天府新区':['南湖公园','天府创新中心']
    },
    '阆中':{'保宁区':['阆中中学','北街口'],
          '七里区':['体育馆','四桥'],
          '江南区':['转盘','木材市场']
    },
    '重庆':{'沙坪坝区':['重庆大学','沙坪坝公园'],
          '渝中区':['洪崖洞','朝天门儿'],
          '永川区':['128','渝西广场']
    }
}
city_index = [(index, key) for index, key in enumerate(dic)]
print(city_index)
city_index.append((len(city_index), '退出'))  # 增加退出选项
while True:
    print('欢迎查询城市信息')
    print('--------------------------------')
    for index,p in city_index:
        print (p[0],p[1])
    get_city = input('请选择查询的索引号：')
    if not get_city.isdigit():
        print('请输入一个数字索引号。')
        continue
    elif int(get_city) >= len(city_index):
        print('输入的数字太大，请重输入。')
        continue
    elif int(get_city) == len(city_index) - 1:
        print('欢迎再次登录')
        break
    else:
        choose_city = city_index[int(get_city)][1]
        area_index = [(index, key) for index, key in enumerate(dic[choose_city])]
        area_index.append((len(area_index), '返回'))
        while True:
            for index,p in area_index:
                print (index,p[1])
            get_area = input('请选择查询的索引号：')
            if not get_area.isdigit():
                print('请输入一个数字索引号。')
                continue
            elif int(get_area) >= len(area_index):
                print('输入的数字太大，请重输入。')
                continue
            elif int(get_area) == len(area_index) - 1:
                print('返回到上一级菜单。')
                break
            else:
                choose_area = area_index[int(get_area)][1]
                print(dic[choose_city][choose_area])
                print('--------------------------------')