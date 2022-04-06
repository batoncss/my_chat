import socket
from for_server import start_server

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 1234))
server_socket.listen()  # включаем прием сообщений
if __name__ == '__main__':
    start_server(server_socket)
