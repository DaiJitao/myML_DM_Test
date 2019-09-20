import socket

''' 服务端 '''

sk = socket.socket()
sk.bind(("localhost", 9999,))
sk.listen(5)  # 至多五个链接
while True:
    conn, address = sk.accept()  # 会被阻塞 conn连接线， address对方地址
    print("conn:", conn, "\n address:", address)
    conn.sendall(bytes("欢迎回来", encoding="utf-8"))
    # conn.sendall("欢迎回来")
