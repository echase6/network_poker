"""Client module manages connection to server.

Hard-coded to work with a fixed port.
"""


import socket

PORTS = [8000, 8001]


def connect_to_server():
    """Module to connect to the server..

    Returns individual serversocket for communication.
    """
    host = input('Host address: ')
    host = '127.0.0.1'
    port = int(input('Port number: '))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))
    return server


def message_from_server(s):
    """Get (wait for) message from server."""
    return s.recv(1024).decode()


def answer_to_server(msg_string, server):
    """Retrieve answer from client.

    Returns string that client entered.
    """
    server.send(msg_string.encode())


def main():
    socket = connect_to_server()
    print(message_from_server(socket))
    answer = input()
    answer_to_server(answer, socket)


if __name__ == '__main__':
    main()
