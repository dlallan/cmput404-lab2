# Lab 2 - TCP Proxy

## Question 1: How do you specify a TCP socket in Python?
In Python with the `socket` module, a TCP socket can be specified by `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.

## Question 2: What is the difference between a client socket and a server socket in Python?
In Python, the sockets of a client and a server are initialized the same way, and then differ in the following calls:
* A client establishes a connection to a server using `socket.connect((HOST, PORT))`.
* A server binds to an address and port using `socket.bind((HOST, PORT))` (the same HOST and PORT the client must `connect` to). Next, a server must then call `socket.listen()` to be notified of an incoming client, then call `socket.accept()` to establish a connection.
* After a server accepts a connection, the two parties can communicate with each other over separate streams using `recv()` and `send()` (other variants are also available in the `socket` module).

## Question 3: How do we instruct the OS to let us reuse the same bind port?
To allow a port to be bound to multiple sockets, the option SO_REUSEADDR or SO_REUSEPORT must be enabled. This can be done with `socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)` or `socket.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)`, respectively.

## Question 4: What information do we get about incoming connections?
Once an incoming connection is `accept`ed, the server receives the IP address and port of the client as the tuple `(address, port)`.

## Question 5: What is returned by `recv()` from the server after it is done sending the HTTP request?
The final `recv()` contains the empty byte `b''`.

## Question 6: Provide a link to your code on GitHub.
https://github.com/dlallan/cmput404-lab2
