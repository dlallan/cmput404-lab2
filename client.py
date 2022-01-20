import socket


def main():
    response_data = b''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('www.google.com', 80))
        client_socket.sendall(
            b'''GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n''')
        client_socket.shutdown(socket.SHUT_WR)

        # Receive the full response
        response_data = b''
        while True:
            buffer = client_socket.recv(4096)
            if buffer:
                response_data = b''.join((response_data, buffer))
            else:
                break

    print(f'response_data ({len(response_data)}):\n', response_data)


if __name__ == '__main__':
    main()
