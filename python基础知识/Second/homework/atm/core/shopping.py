flag = True
product_order = [['Iphone8',6888],['MacPre',12000],['Mi6',2499],['coffee',31],['Book',80]]
salary = input("请输入您的工资：")
shopping_cart = []

while True:
    print ("-------商品列表-------")
    for index,p in enumerate(product_order):
        print (index,p[0],p[1])
    choice = input("输入想要的商品编号：")
    if choice.isdigit():
        choice = int(choice)

    elif choice == "q":
        print("-------您已购买以下商品--------")
        for index, p in enumerate(shopping_cart):
            print(index, p[0], p[1])
        print("余额：" + str(salary))
        print("欢迎下次再来！")
        break