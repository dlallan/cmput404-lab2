import socket


def main():
    response_data = b''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('www.google.com', 80))
        client_socket.sendall(
            b'''GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n''')
        response_data = client_socket.recv(4096)

    print(f'response_data ({len(response_data)}):\n', response_data)


if __name__ == '__main__':
    main()
