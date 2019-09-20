import socket

obj = socket.socket()

res = obj.connect(("localhost", 9999,))
res = obj.recv(1024)  # 接收不到，僵持住，阻塞
print(res)
res = str(res, encoding='utf-8')
print(res)
obj.close()
