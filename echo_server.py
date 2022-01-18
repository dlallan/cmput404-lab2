import socket


def main():
    HOST = ''
    PORT = 8888
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f'Listening on port {PORT}')
        server_socket.listen()
        client_conn, client_addr = server_socket.accept()
        with client_conn:
            print(f"client address: {client_addr}")
            while True:
                client_data = client_conn.recv(4096)
                if not client_data:
                    break
                client_conn.sendall(client_data)


if __name__ == '__main__':
    main()
