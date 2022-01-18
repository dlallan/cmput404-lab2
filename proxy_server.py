import socket


def main():
    proxy_addr = ('', 8001)
    google_addr = ('www.google.com', 80)
    with socket.create_server(proxy_addr) as proxy:
        proxy.listen()
        client_conn, client_addr = proxy.accept()
        print(f"Connected to client at {client_addr}")
        with socket.create_connection(google_addr) as google_conn:
            client_data = b''
            while True:
                data = client_conn.recv(4096)
                # print('data from client:')
                # print(data)
                if data[-4:] == b'\r\n\r\n':
                    client_data = b''.join((client_data, data))
                    break
                else:
                    b''.join((client_data, data))

            if client_data:
                google_conn.sendall(client_data)

            google_data = b''
            while True:
                data = google_conn.recv(4096)
                # print("response from google:")
                # print(data)
                google_data = b''.join((google_data, data))
                if data[-4:] == b'\r\n\r\n':
                    break

            if google_data:
                client_conn.sendall(google_data)


if __name__ == '__main__':
    main()
