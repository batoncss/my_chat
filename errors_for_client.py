def check_conn_err(user_socket):
    user_socket.close()
    print('Соединение с сервером разорвано. Требуется перезапуск приложения.')
    exit()


def server_is_off():
    print('Нет соединения с сервером. Обратитесь к администратору.')
    exit()
