import socket
from threading import Thread

users = []


class User(object):
    def __init__(self, user_socket, user_address):
        self.socket = user_socket
        self.address = user_address


def message_for_all(data):
    for user in users:
        user.send(data)


def check_messages(user, address):
    while True:
        data = user.recv(2048)
        if data:
            message = f'Пользователь {address} отправил сообщение {data.decode("utf-8")}'
            print(message)
            message_for_all(message.encode("utf-8"))


def start_server():
    while True:
        user_socket, user_address = server_socket.accept()
        print(f'Пользователь {user_address} подключился!')
        users.append(user_socket)
        listening_users = Thread(target=check_messages, args=(user_socket, user_address))
        listening_users.start()


server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 1234))
server_socket.listen()  # включаем прием сообщений

if __name__ == '__main__':
    start_server()
