from http import server
import socket


def main():
    server_addr = ('localhost', 8001)
    with socket.create_connection(server_addr) as conn:
        conn.sendall(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
        conn.shutdown(socket.SHUT_WR)
        
        proxy_data = b''
        while True:
            data = conn.recv(4096)
            if data:
                proxy_data = b''.join((proxy_data, data))
            else:
                break

        if proxy_data:
            print('Data received from proxy:\n', proxy_data)


if __name__ == '__main__':
    main()
