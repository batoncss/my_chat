import socket
from threading import Thread


class User(object):
    def __init__(self, user_socket, user_address):
        self.socket = user_socket
        self.address = user_address



def logging(data):
    file_for_log = open('syslog.txt', 'a')
    file_for_log.write(data + "\n")
    file_for_log.close()
def message_for_all(data):
    for user in users:
        user.send(data)
        logging(data.decode('utf-8'))


def check_messages(user, address):
    while True:
        data = user.recv(2048)
        if data:
            if "/имя" in data.decode("utf-8"):
                name = data.decode("utf-8")[5:]
                name_users[address[1]] = name
                print(name_users)
            else:
                if address[1] in name_users:
                    name_sender = name_users[address[1]]
                else:
                    name_sender = address[1]
                message = f'{name_sender}: {data.decode("utf-8")}'
                print(message)
                message_for_all(message.encode("utf-8"))


def start_server():
    while True:
        user_socket, user_address = server_socket.accept()
        print(f'Пользователь {user_address} подключился!')
        logging(f'Пользователь {user_address} подключился!')
        users.append(user_socket)
        listening_users = Thread(target=check_messages, args=(user_socket, user_address))
        listening_users.start()

users = []
name_users = {}
server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 1234))
server_socket.listen()  # включаем прием сообщений
if __name__ == '__main__':
    start_server()

