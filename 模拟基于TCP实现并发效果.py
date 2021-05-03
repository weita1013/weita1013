import socket
from threading import Thread

server = socket.socket()  # 默认family为AF_INET，type为SOCK_STREAM
server.bind(('127.0.0.1', 8000))
server.listen(5)


def talk():
    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:
                break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()


# 链接循环
while True:
    conn, addr = server.accept()  # accept返回socket object, address info
    t = Thread(target=talk())
    t.start()
