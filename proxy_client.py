from http import server
import socket


def main():
    server_addr = ('localhost', 8001)
    with socket.create_connection(server_addr) as conn:
        conn.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
        proxy_data = b''
        while True:
            data = conn.recv(4096)
            proxy_data = b''.join((proxy_data, data))
            if data[-4:] == b'\r\n\r\n':
                break

        if proxy_data:
            print(proxy_data)


if __name__ == '__main__':
    main()
