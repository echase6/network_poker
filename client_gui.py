"""Client GUI for pretty displaying of the table.

This is purely a rendering (display) function.  No inputs are taken.

display_image() -- updates the display
display_blank_table() -- shows a blank table (just the felt)
display_card() -- displays one card on the table
display_name() -- displays the name on the table
get_card_image() -- gets an image of the card face
get_card_back() -- gets an image of the back of a card
make_chip_tray() -- creates an image of a chip tray, based on value
display_chip_tray() -- displays the chip tray for an individual player
display_pot_tray() -- displays the pot tray
update_table() -- updates the entire table (cards, names, chip trays)
"""

from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import Tk, Canvas
from card import Card, SUITS, RANKS
from chip import calc_chips, DENOMINATIONS, DENOM_COLORS
from chip import WHITE, BLACK


CARD_WIDTH = 72
CARD_HEIGHT = 100


def display_image(canvas, table_img):
    """Update the display.

    Updates canvas and table_img in-place.
    """
    photo_image = ImageTk.PhotoImage(table_img)
    canvas.pack()
    canvas.create_image(500, 300, image=photo_image)
    canvas.update()


def display_window():
    """Open the window to show an empty table."""
    table_img = Image.open('./images/poker-table-felt.jpg')
    window_handle = Tk()
    window_handle.wm_title('Networked Poker Game')
    canvas = Canvas(window_handle, width=1000, height=600)
    display_image(canvas, table_img)
    return canvas, table_img


def display_card(canvas, table_img, index, player_index, card_im):
    """Add card to table canvas."""
    x_loc = 350 + index * (CARD_WIDTH + 28)
    y_loc = 100 + player_index * 280
    table_img.paste(card_im, (x_loc, y_loc))
    display_image(canvas, table_img)


def display_name(canvas, table_img, name, player_index):
    """Add names to the table."""
    x_loc = 450
    y_loc = 50 + player_index * 450
    font = ImageFont.truetype('arial.ttf', 40)
    draw = ImageDraw.Draw(table_img)
    draw.text((x_loc, y_loc), name, font=font, fill=(255, 128, 128, 255))
    display_image(canvas, table_img)


def display_chip_tray(canvas, table_img, value, player_index):
    """Display the chip tray."""
    x_loc = 50
    y_loc = 50 + player_index * 400
    tray_img = make_chip_tray_image(value)
    table_img.paste(tray_img, (x_loc, y_loc))
    display_image(canvas, table_img)


def display_pot_tray(canvas, table_img, value):
    """Display the pot tray."""
    x_loc = 400
    y_loc = 250
    tray_img = make_chip_tray_image(value)
    table_img.paste(tray_img, (x_loc, y_loc))
    display_image(canvas, table_img)


def calc_chip_box(denom_index, chip_count):
    """Calculate the location of the chip in the tray.

    >>> calc_chip_box(1, 2):
    (80, 30, 120, 70)
    """
    chip_dia = 40
    margin = 20
    chip_step = 5
    x_loc = margin + denom_index * (chip_dia + margin)
    y_loc = 40 - chip_count * chip_step
    chip_box = (x_loc, y_loc, x_loc + chip_dia, y_loc + chip_dia)
    return chip_box


def calc_chip_text_box(x_loc, y_loc, tray_img, denom, font):
    """Calculate the position of the label that goes on top of the chip."""
    (txt_x, txt_y) = ImageDraw.Draw(tray_img).textsize(denom, font=font)
    return x_loc + 20 - txt_x // 2, y_loc + 20 - txt_y // 2


def make_chip_tray_image(value):
    """Return image of chip tray, based on value."""
    tray_img = Image.new('RGB', (200, 100), (0, 128, 0))
    ImageDraw.Draw(tray_img).rectangle((0, 0, 199, 99),
                                       outline=WHITE, fill=None)
    font = ImageFont.truetype('arial.ttf', 20)
    chip_dict = calc_chips(value)
    for index, denom in enumerate(DENOMINATIONS):
        for chip_count in range(chip_dict[denom]):
            chip_box = calc_chip_box(index, chip_count)
            ImageDraw.Draw(tray_img).ellipse(chip_box, fill=DENOM_COLORS[index],
                                             outline=BLACK)
            (x_loc, y_loc, x_may, y_max) = chip_box
            text_loc = calc_chip_text_box(x_loc, y_loc, tray_img, denom, font)
            ImageDraw.Draw(tray_img).text(text_loc, denom,
                                          font=font, fill=BLACK)
    return tray_img


def calc_card_row_col(card):
    """Find the crop window for a particular card.

    >>> calc_card_row_col(Card('H', '8'))
    (0, 7)
    """
    row = SUITS.index(card.suit)
    col = (1 + RANKS.index(card.rank)) % 13
    return row, col


def calc_card_crop_box(row, col):
    """Return the crop box for a particular row and col choice.

    >>> calc_card_crop_box(2, 4)
    (288, 200, 360, 300)
    """
    box = (col * CARD_WIDTH, row * CARD_HEIGHT,
           (col + 1) * CARD_WIDTH, (row + 1) * CARD_HEIGHT)
    return box


def get_card_image(card):
    """Return the image of the face of a card."""
    deck_im = Image.open('./images/Deck.png')
    row, col = calc_card_row_col(card)
    box = calc_card_crop_box(row, col)
    return deck_im.crop(box)


def get_card_back():
    """Return an image of the back of a card."""
    deck_im = Image.open('./images/Deck.png')
    box = calc_card_crop_box(4, 5)
    return deck_im.crop(box)


def update_table(table, canvas, table_img, port):
    """Add images to the table, as they are present in the table container.

    Items to display: Name, chip tray, pot, cards
    """
    table_img = Image.open('./images/poker-table-felt.jpg')
    display_image(canvas, table_img)
    for player_index, player in enumerate(table.players):
        display_name(canvas, table_img, player.name, player_index)
        display_chip_tray(canvas, table_img, player.stash.value, player_index)
        display_pot_tray(canvas, table_img, table.pot.value)
        for card_index, card in enumerate(player.hand.hand_list):
            if player.port != port and card_index == 0:
                card_img = get_card_back()
            else:
                card_img = get_card_image(card)
            display_card(canvas, table_img, card_index, player_index, card_img)


def main():
    canvas, table_img = display_blank_table()
    display_name(canvas, table_img, 'Eric', 0)
    display_chip_tray(canvas, table_img, 137, 0)
    display_pot_tray(canvas, table_img, 49)
    for i in range(5):
        card_img = get_card_image(Card('H', '6'))
        display_card(canvas, table_img, i, 0, card_img)
    while True:
        pass

if __name__ == '__main__':
    main()
