import socket
from threading import Thread


def check_messages(user):
    while True:
        data = user.recv(1024)
        print(data.decode('utf-8'))


def send_for_server():
    listening_server = Thread(target=check_messages, args=(user_socket,))
    listening_server.start()
    while True:
        message = input()
        user_socket.send(message.encode('utf-8'))



# print('Как Вас зовут?\n')
# user_name = input()
user_socket = socket.socket()
user_socket.connect(('127.0.0.1', 1234))
if __name__ == '__main__':
    send_for_server()
