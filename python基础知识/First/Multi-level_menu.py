#/usr/local/bin/env python3
#coding:utf-8

city = {
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
city_list = list(zone.keys())
while True:
    print(" 市 ".center(50,'-'))
    for i in city_list:
        print(i)
    pro_id = input("请输入市编号,或输入q(quit)退出：")
    if pro_id.isdigit():

