import socket


client = socket.socket()
client.connect(('127.0.0.1', 8000))

while True:
    client.send('aah'.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

