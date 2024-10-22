import socket

class TCPClient:
    def __init__(self, server_ip, server_port):
        # Initialize client socket with IPv4 (AF_INET) and TCP (SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (server_ip, server_port)

    def connect(self):
        # Establish connection to the TCP server
        self.client_socket.connect(self.server_address)
        print(f'Connected to TCP server at {self.server_address}')

    def send_message(self, message):
        # Send a message to the server
        self.client_socket.sendall(message.encode())
        print(f'Sent message: {message}')

    def receive_message(self):
        # Receive a message from the server
        data = self.client_socket.recv(1024)
        print(f'Received message: {data.decode()}')

    def close(self):
        # Close the client socket connection
        self.client_socket.close()
        print('Closed TCP connection')


class TCPServer:
    def __init__(self, server_ip, server_port):
        # Initialize server socket with IPv4 (AF_INET) and TCP (SOCK_STREAM)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (server_ip, server_port)
        # Bind the server socket to the IP and port
        self.server_socket.bind(self.server_address)

    def start(self):
        # Start listening for incoming connections (with backlog of 1)
        self.server_socket.listen(1)
        print(f'TCP Server listening on {self.server_address}')
        # Accept a connection from a client
        self.connection, self.client_address = self.server_socket.accept()
        print(f'Connected to {self.client_address}')

    def receive_message(self):
        # Receive a message from the client
        data = self.connection.recv(1024)
        print(f'Received message: {data.decode()}')
        return data

    def send_message(self, message):
        # Send a message to the client
        self.connection.sendall(message.encode())
        print(f'Sent message: {message}')

    def close(self):
        # Close the connection with the client
        self.connection.close()
        print('Closed TCP connection')


# Example Usage of TCP Classes
# Server (run in one process/thread)
# tcp_server = TCPServer('localhost', 65432)
# tcp_server.start()
# data = tcp_server.receive_message()
# tcp_server.send_message(data.decode())
# tcp_server.close()

# Client (run in a separate process/thread)
# tcp_client = TCPClient('localhost', 65432)
# tcp_client.connect()
# tcp_client.send_message('Hello from TCP Client')
# tcp_client.receive_message()
# tcp_client.close()


import socket

class UDPClient:
    def __init__(self, server_ip, server_port):
        # Initialize client socket with IPv4 (AF_INET) and UDP (SOCK_DGRAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (server_ip, server_port)

    def send_message(self, message):
        # Send a message to the UDP server (no connection setup needed)
        self.client_socket.sendto(message.encode(), self.server_address)
        print(f'Sent message: {message}')

    def receive_message(self):
        # Receive a message from the server
        data, server = self.client_socket.recvfrom(1024)
        print(f'Received message: {data.decode()} from {server}')

    def close(self):
        # Close the client socket
        self.client_socket.close()
        print('Closed UDP connection')


class UDPServer:
    def __init__(self, server_ip, server_port):
        # Initialize server socket with IPv4 (AF_INET) and UDP (SOCK_DGRAM)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (server_ip, server_port)
        # Bind the server socket to the IP and port
        self.server_socket.bind(self.server_address)

    def receive_message(self):
        # Receive a message from any client
        data, client_address = self.server_socket.recvfrom(1024)
        print(f'Received message: {data.decode()} from {client_address}')
        return data, client_address

    def send_message(self, message, client_address):
        # Send a message to the client (based on client address)
        self.server_socket.sendto(message.encode(), client_address)
        print(f'Sent message: {message} to {client_address}')

    def close(self):
        # Close the server socket
        self.server_socket.close()
        print('Closed UDP connection')


# Example Usage of UDP Classes
# Server (run in one process/thread)
# udp_server = UDPServer('localhost', 65433)
# data, client_address = udp_server.receive_message()
# udp_server.send_message(data.decode(), client_address)
# udp_server.close()

# Client (run in a separate process/thread)
# udp_client = UDPClient('localhost', 65433)
# udp_client.send_message('Hello from UDP Client')
# udp_client.receive_message()
# udp_client.close()


'''
Key Differences Between the Classes:

TCP (Connection-Oriented):

In TCPClient, connect() is required to establish a connection before sending or receiving data.

In TCPServer, accept() blocks until a client connects. Once connected, data is exchanged with sendall() and recv(), and the connection remains open until explicitly closed.

TCP uses a stream-oriented model, meaning data flows continuously between the server and client.

Higher overhead due to connection establishment, error checking, and flow control.





UDP (Connectionless):

In UDPClient, there is no need to establish a connection. Data is sent directly to the server using sendto().

In UDPServer, it can receive messages from multiple clients without needing to establish individual connections using recvfrom().

UDP is datagram-oriented, meaning each packet is sent individually, without connection setup or guarantee of delivery.

Lower overhead, but lacks the reliability and ordering of TCP.

Example Usage:
TCP: Use these classes for applications requiring reliable communication like file transfers, chat applications, or HTTP servers.
UDP: Use these classes for fast, connectionless communication like video streaming, gaming, or DNS lookups.


'''