"""Client GUI for pretty displaying of the table.

This is purely a rendering (display) function.  No inputs are taken.

Hard-coded to work with a fixed address and port, entered at startup.

connect_to_server() connects the client to the server
message_from_server() displays a message from the server
answer_to_server() inquires the user and sends the response to the server
render_table() unpacks the shipped JSON version of the table and displays it
process_server_message() interprets the incoming info and acts appropriately

display_image()
display_blank_table()
display_card()
display_name()
get_card_image()
get_card_back()
update_table()
"""

from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import PhotoImage, Tk, Canvas
from card import SUITS, RANKS
import socket
import jsonpickle


CARD_WIDTH = 72
CARD_HEIGHT = 100
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


def process_server_message(msg, server, canvas, table_img, port):
    """Analyzes and acts on the content of a message from the server.

    Valid actions are:
      rendering a table (Table JSON was sent)
      asking a question and sending response to server (msg ends with a ?)
      displaying a message
    """
    if msg[0] == '{':
        update_table(msg, canvas, table_img, port)
    elif msg[-1] == '?':
        answer = input(msg)
        answer_to_server(answer, server)
    else:
        print(msg)


def display_image(canvas, table_img):
    """Update the display.

    Updates canvas and table_img in-place.
    """
    photo_image = ImageTk.PhotoImage(table_img)
    canvas.pack()
    canv_image = canvas.create_image(500, 300, image=photo_image)
    canvas.update()


def display_blank_table():
    """Open the window to show an empty table."""
    table_img = Image.open('..\images\poker-table-felt.jpg')
    window_handle = Tk()
    window_handle.wm_title('Networked Poker Game')
    canvas = Canvas(window_handle, width=1000, height=600)
    display_image(canvas, table_img)
    return canvas, table_img


def display_card(canvas, table_image, index, player_index, card_im):
    """Add card to table canvas."""
    x_loc = 250 + index * (CARD_WIDTH + 28)
    y_loc = 100 + player_index * 280
    table_image.paste(card_im, (x_loc, y_loc))
    display_image(canvas, table_image)


def display_name(canvas, table_img, name, player_index):
    """Add names to the table."""
    x_loc = 450
    y_loc = 50 + player_index * 450
    font = ImageFont.truetype('arial.ttf', 40)
    draw = ImageDraw.Draw(table_img)
    draw.text((x_loc, y_loc), name, font=font, fill=(255,128,128,255))
    display_image(canvas, table_img)


def get_card_image(card):
    """Return the image of the face of a card."""
    deck_im = Image.open('..\images\Deck.png')
    row = SUITS.index(card.suit)
    col = RANKS.index(card.rank)
    box = (col * CARD_WIDTH, row * CARD_HEIGHT,
           (col + 1) * CARD_WIDTH, (row + 1) * CARD_HEIGHT)
    card_im = deck_im.crop(box)
    return card_im


def get_card_back():
    """Return an image of the back of a card."""
    deck_im = Image.open('..\images\Deck.png')
    row = 4
    col = 5
    box = (col * CARD_WIDTH, row * CARD_HEIGHT,
           (col + 1) * CARD_WIDTH, (row + 1) * CARD_HEIGHT)
    card_im = deck_im.crop(box)
    return card_im


def update_table(table_json, canvas, table_img, port):
    """Add images to the table, as they are present in the table_json file."""
    table = jsonpickle.decode(table_json)
    for player_index, player in enumerate(table.players):
        display_name(canvas, table_img, player.name, player_index)
        for card_index, card in enumerate(player.hand.hand_list):
            if player.port != port and card_index == 0:
                card_img = get_card_back()
            else:
                card_img = get_card_image(card)
            display_card(canvas, table_img, card_index, player_index, card_img)


def main():
    socket, port = connect_to_server()
    canvas, table_image = display_blank_table()
    while True:
        message = message_from_server(socket)
        if len(message) > 0:
            process_server_message(message, socket, canvas, table_image, port)


if __name__ == '__main__':
    main()
