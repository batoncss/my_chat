from threading import Thread

users = []
name_users = {}


def logging(data):
    file_for_log = open('syslog.txt', 'a')
    file_for_log.write(data + "\n")
    file_for_log.close()


def message_for_all(data):
    for user in users:
        try:
            user.send(data)
        except ConnectionResetError:
            continue
        except BrokenPipeError:
            continue
    print(data.decode('utf-8'))
    logging(data.decode('utf-8'))


def check_messages(user, address):
    while True:
        try:
            data = user.recv(2048)
        except ConnectionResetError:
            break
        if data:
            if "/имя" in data.decode("utf-8"):
                name = data.decode("utf-8")[5:]
                name_users[address[1]] = name
                print(name_users)
                logging(str(name_users))
            else:
                if address[1] in name_users:
                    name_sender = name_users[address[1]]
                else:
                    name_sender = address[1]
                message = f'{name_sender}: {data.decode("utf-8")}'
                message_for_all(message.encode("utf-8"))


def start_server(server_socket):
    print("Сервер запущен!")
    while True:
        user_socket, user_address = server_socket.accept()
        print(f'Пользователь {user_address} подключился!')
        logging(f'Пользователь {user_address} подключился!')
        users.append(user_socket)
        listening_users = Thread(target=check_messages, args=(user_socket, user_address))
        listening_users.start()
