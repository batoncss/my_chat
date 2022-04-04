import socket
from threading import Thread


def check_messages(user):
    while True:
        data = user.recv(1024)
        print(data.decode('utf-8'))

def rename(user):
    print('Как Вас зовут?')
    name = '/имя ' + input()
    user.send(name.encode('utf-8'))
    print(f'*Ваше имя изменено на {name[5:]}*')
    return name[5:]


def send_for_server():
    listening_server = Thread(target=check_messages, args=(user_socket,))
    listening_server.start()
    while True:
        message = input()
        if '/имя' in message:
            rename(user_socket)
        else:
            user_socket.send(message.encode('utf-8'))

user_socket = socket.socket()
user_socket.connect(('127.0.0.1', 1234))

if __name__ == '__main__':
    print(f'Здравствуйте, {rename(user_socket)}. Вы успешно подлкючились к чату.')
    send_for_server()
