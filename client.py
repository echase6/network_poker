"""Client main and modules for communicating with server and displaying table.

Hard-coded to work with a fixed address and port, entered at startup.

connect_to_server() connects the client to the server
message_from_server() displays a message from the server
answer_to_server() inquires the user and sends the response to the server
render_table() unpacks the shipped JSON version of the table and displays it
process_server_message() interprets the incoming info and acts appropriately

"""

# from PIL import Image, ImageTk, ImageFont, ImageDraw
# from tkinter import PhotoImage, Tk, Canvas
from card import SUITS, RANKS
from chip import calc_chips, DENOMINATIONS, DENOM_COLORS
from client_gui import display_image, display_card
from client_gui import display_name, get_card_back, get_card_image
from client_gui import update_table, display_chip_tray, display_pot_tray
from client_gui import make_chip_tray_image
from client_gui import update_table, display_window
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
    return s.recv(2048).decode()


def answer_to_server(msg_string, server):
    """Sends answer to server."""
    server.send(msg_string.encode())


def process_server_message(msg, server, canvas, table_img, port):
    """Analyzes and acts on the content of a message from the server.

    Valid actions are:
      rendering a table (Table JSON was sent)
      asking a question and sending response to server (msg ends with a ?)
      displaying a message
    """
    if msg[0] == '{':
        table = jsonpickle.decode(msg)
        update_table(table, canvas, table_img, port)
    elif msg[-1] == '?':
        answer = input(msg)
        answer_to_server(answer, server)
    else:
        print(msg)


def main():
    skt, port = connect_to_server()
    canvas, table_image = display_window()
    while True:
        message = message_from_server(skt)
        if len(message) > 0:
            process_server_message(message, skt, canvas, table_image, port)


if __name__ == '__main__':
    main()
