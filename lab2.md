# Lab 2 - TCP Proxy

## Question 1: How do you specify a TCP socket in Python?
In Python with the `socket` module, a TCP socket can be specified by `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`.

## Question 2: What is the difference between a client socket and a server socket in Python?
In Python, the sockets of a client and a server are initialized the same way, and then differ in the following calls:
* A client establishes a connection to a server using `socket.connect((HOST, PORT))`.
* A server binds to an address and port using `socket.bind((HOST, PORT))` (the same HOST and PORT the client must `connect` to). Next, a server must then call `socket.listen()` to be notified of an incoming client, then call `socket.accept()` to establish a connection.
* After a server accepts a connection, the two parties can communicate with each other over separate streams using `recv()` and `send()` (other variants are also available in the `socket` module).

## Question 3: How do we instruct the OS to let us reuse the same bind port?
The method `socket.bind((HOST, PORT))` will ensure that the socket will be bound to `PORT` each time the program is run.
**TODO: socket.setsockopt(level, optname, value: int) ????**

## Question 4: What information do we get about incoming connections?
Once an incoming connection is `accept`ed, the server receives the address and port of the client as the tuple `(address, port)`.

## Question 5: What is returned by `recv()` from the server after it is done sending the HTTP request?
The response from the server is an HTTP response. If the request was successful, the response should start with a response line like `HTTP/1.1 200 OK` followed by the response header and possibly an entity the content requested by the client.
**TODO: What scenario is this server handling HTTP requests for?**

## Question 6: Provide a link to your code on GitHub.

