import socket
import multiprocessing


def _handle_client(client_conn: socket.socket) -> None:
    buffer_size = 4096
    google_addr = ('www.google.com', 80)

    client_data = b''
    while True:
        buffer = client_conn.recv(buffer_size)
        if buffer:
            client_data = b''.join((client_data, buffer))
        else:
            break

    if not client_data:
        return

    with socket.create_connection(google_addr) as google_conn:
        google_conn.sendall(client_data)
        google_conn.shutdown(socket.SHUT_WR)

        google_data = b''
        while True:
            buffer = google_conn.recv(buffer_size)
            if buffer:
                google_data = b''.join((google_data, buffer))
            else:
                break

        if google_data:
            client_conn.sendall(google_data)
            client_conn.shutdown(socket.SHUT_WR)


def main():
    proxy_addr = ('', 8001)
    with socket.create_server(proxy_addr) as proxy:
        proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            # listen until manually interrupted by user
            while True:
                proxy.listen()
                client_conn, client_addr = proxy.accept()
                print(f"Connected to client at {client_addr}")
                process = multiprocessing.Process(
                    target=_handle_client, args=(client_conn,))
                process.start()

        except KeyboardInterrupt:
            print('Shutting down')
            proxy.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    main()
