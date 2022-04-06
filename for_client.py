from threading import Thread
from errors_for_client import check_conn_err


def check_messages(user_socket):
    while True:
        try:
            data = user_socket.recv(1024)
        except ConnectionResetError:
            check_conn_err(user_socket)
        except ConnectionAbortedError:
            check_conn_err(user_socket)
        except OSError:
            check_conn_err(user_socket)
        if data:
                print(data.decode('utf-8'))


def rename(user_socket):
    print('Как Вас зовут?')
    name = '/имя ' + input()
    try:
        user_socket.send(name.encode('utf-8'))
    except ConnectionResetError:
        check_conn_err(user_socket)
    print(f'*Ваше имя изменено на {name[5:]}*')
    return name[5:]


def send_for_server(user_socket):
    listening_server = Thread(target=check_messages, args=(user_socket,))
    listening_server.start()
    while True:
        message = input()
        if '/имя' in message:
            rename(user_socket)
        else:
            try:
                user_socket.send(message.encode('utf-8'))
            except OSError:
                check_conn_err(user_socket)