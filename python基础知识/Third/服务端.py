import socket

#1 买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(phone)

#2 绑定手机卡
phone.bind(('127.0.0.1',8080))   #0-65535:0-1024给操作系统用

#3 开机
phone.listen(5)#5代表最大挂起的链接数   同时接几个电话

#4 等电话
# res = phone.accept()
conn,client_addr = phone.accept()

#5 收发消息
data=conn.recv(1024)#单位：bytes 1024代表最大接受1024个bytes
print('客户端的数据',data)

conn.send(data.upper())

#6 挂电话
conn.close()

#7 关机
phone.close()

print('zhangchuhan')