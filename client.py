"""Client main and modules for communicating with server and displaying table.

Run this module on the client computers (i.e., computers for each player)

Hard-coded to work with a fixed address, entered at startup.  This can be
  changed in the connect_to_server() module.
Valid ports are 8000 and 8001.  It is more stable if they are the order of the
  connecting clients, although not 100% necessary.


connect_to_server() connects the client to the server
message_from_server() displays a message from the server
answer_to_server() inquires the user and sends the response to the server
render_table() unpacks the shipped JSON version of the table and displays it
process_server_message() interprets the incoming info and acts appropriately
"""

from PIL import Image, ImageTk, ImageFont, ImageDraw
from card import SUITS, RANKS
from chip import calc_chips, DENOMINATIONS, DENOM_COLORS
from client_gui import update_table, display_window, display_image
import socket
import jsonpickle


PORTS = [8000, 8001]


def connect_to_server():
    """Module to connect the client to the server.

    Returns individual serversocket for communication.
    """
    host = input('Host address: ')
    if host == '':
        host = '127.0.0.1'
    port = int(input('Port number: '))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))
    return server, port


def message_from_server(s):
    """Get (wait for) message from server."""
    return s.recv(2048).decode()


def answer_to_server(msg_string, server):
    """Sends answer to server."""
    msg_string += ' '  # make sure something goes across
    server.send(msg_string.encode())


def process_server_message(msg, server, canvas, table_img, port):
    """Analyzes and acts on the content of a message from the server.

    Valid actions are:
      rendering a table (Table JSON was sent, starts with a {)
      asking a question and sending response to server (msg contains a ?)
      displaying a message (if above not true)
    """
    if msg[0] == '{':
        table = jsonpickle.decode(msg)
        update_table(table, canvas, table_img, port)
    elif '?' in msg:
        answer = input(msg)
        answer_to_server(answer, server)
    else:
        print(msg)


def main():
    skt, port = connect_to_server()
    table_img = Image.open('./images/poker-table-felt.jpg')
    canvas = display_window()
    display_image(canvas, table_img)
    while True:
        message = message_from_server(skt)
        if len(message) > 0:
            process_server_message(message, skt, canvas, table_img, port)


if __name__ == '__main__':
    main()
