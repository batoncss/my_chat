from socket import socket
from for_client import send_for_server, rename, check_conn_err
from errors_for_client import server_is_off

user_socket = socket()
try:
    user_socket.connect(('127.0.0.1', 1234))
except ConnectionRefusedError:
    server_is_off()

if __name__ == '__main__':
    print(f'Здравствуйте, {rename(user_socket)}. Вы успешно подлкючились к чату.')
    send_for_server(user_socket)
