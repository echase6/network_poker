"""Client module manages connection to server.

Hard-coded to work with a fixed address and port, entered at startup.

connect_to_server() connects the client to the server
message_from_server() displays a message from the server
answer_to_server() inquires the user and sends the response to the server
render_table() unpacks the shipped JSON version of the table and displays it
process_server_message() interprets the incoming info and acts appropriately
"""


import socket
import jsonpickle

PORTS = [8000, 8001]


def connect_to_server():
    """Module to connect the client to the server.

    Returns individual serversocket for communication.
    """
    host = input('Host address: ')
    host = '127.0.0.1'
    port = int(input('Port number: '))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))
    return server, port


def message_from_server(s):
    """Get (wait for) message from server."""
    return s.recv(1024).decode()


def answer_to_server(msg_string, server):
    """Sends answer to server."""
    server.send(msg_string.encode())


def render_table(table_json):
    """Render the table from received json file.

    This shares code from the previously-written Table class __str__()
    function, so this should be put in a separate module to be common to both.
    """
    table = jsonpickle.decode(table_json)
    out_string_list = []
    for player in table.players:
        out_string = ''
        out_string += 'Name: {:10s}  Hand: X-X '.format(player.name)
        for card in player.hand.hand_list[1:]:
            out_string += '{}-{} '.format(card.rank, card.suit).ljust(20)
        out_string += 'Stash: {}   Status: {}'.format(player.stash.value,
                                                      player.status)
        out_string_list += [out_string]
    pot_string = ' '*10 + 'Pot: {}'.format(table.pot.value)
    return '\n\n'.join([out_string_list[0], pot_string, out_string_list[1]])


def process_server_message(msg, server):
    """Analyzes and acts on the content of a message from the server.

    Valid actions are:
      rendering a table (Table JSON was sent)
      asking a question and sending response to server (msg ends with a ?)
      displaying a message
    """
    if msg[0] == '{':  # Don't expect this to work just yet...
        print(render_table(msg))
    elif msg[-1] == '?':
        answer = input(msg)
        answer_to_server(answer, server)
    else:
        print(msg)


def main():
    socket, port = connect_to_server()
    while True:
        message = message_from_server(socket)
        if len(message) > 0:
            process_server_message(message, socket)


if __name__ == '__main__':
    main()
