from cards import get_all_cards
from card_generator import generate_card
import re

def main():
    html = generate_html_with_all_cards()
    write_in_file("view/generated_view.html", html)

def generate_html_with_all_cards():
    gallery = read_content("view/gallery.html")
    cards_html = ""
    for card in get_all_cards():
        cards_html += generate_card(card)

    return re.sub("python-cards", cards_html, gallery)

def read_content(file):
    with open(file, "r") as fh:
        return fh.read()

def write_in_file(file, html):
    with open(file, "w") as fh:
        fh.write(html)


main()
