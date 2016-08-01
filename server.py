"""Server module manages connections to clients.

Hard-coded to work with two clients, at fixed ports.

start_server() starts the server sockets for each member of PORTS
connect_client() connects each individual client, when they request to.
message_to_client() sends a message to an individual client
answer_from_client() reads back a message from an individual client
send_table_to_client() packs and sends the table to the client for rendering
"""


import socket
import jsonpickle

PORTS = [8000, 8001]


def get_server_ip():
    """Get the internet IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('gmail.com', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip



def start_server():
    """This module starts the server sockets for the ports in PORTS.

    host and ports are hard-coded (no discovery).
    Returns list of sockets to be used for connecting individual clients.
    """
    sockets = []
    host = "127.0.0.1"
    # host = get_server_ip()
    print('Host: {}'.format(host))
    print('Ports: {}'.format(PORTS))
    for port in PORTS:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((host, port))
        serversocket.listen(5)
        sockets += [serversocket]
    print('server started and listening')
    return sockets


def connect_client(serversocket):
    """Module to connect an individual client.

    Returns individual clientsocket for communication.
    """
    (clientsocket, address) = serversocket.accept()
    print('connection to {} found!'.format(address))
    return clientsocket


def message_to_client(msg_string, clientsocket):
    """Send message to client."""
    clientsocket.send(msg_string.encode())


def answer_from_client(clientsocket):
    """Retrieve answer from client.

    Returns string that client entered.
    """
    ans_string = clientsocket.recv(1024).decode()
    return ans_string


def send_table_to_client(table, client):
    """Sends the table to the client for rendering."""
    table_json = jsonpickle.encode(table)
    client.send(table_json.encode())


def main():
    sockets = start_server()
    clients = [connect_client(s) for s in sockets]
    for c in clients:
        message_to_client('What do you want to say?', c)
        print(answer_from_client(c))

if __name__ == '__main__':
    main()
