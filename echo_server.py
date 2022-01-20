import socket


def main():
    HOST = ''
    PORT = 8001
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        print(f'Listening on port {PORT}')

        # Listen until manually interrupted by user
        server_socket.listen()
        try:
            while True:
                client_conn, client_addr = server_socket.accept()
                with client_conn:
                    print(f'Connected to client at address: {client_addr}')
                    while True:
                        client_data = client_conn.recv(1)
                        if not client_data:
                            client_conn.shutdown(socket.SHUT_RDWR)
                            break
                        client_conn.sendall(client_data)
                        
        except KeyboardInterrupt:
            print('Shutting down')
            server_socket.shutdown(socket.SHUT_RDWR)


if __name__ == '__main__':
    main()
