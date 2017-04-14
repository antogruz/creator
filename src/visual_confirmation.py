from cards import get_all_cards
from card_generator import generate_card
import re

def main():
    html = generate_html_with_all_cards()
    write_in_file("view/generated_view.html", html)



class Galerie:
    def __init__(self):
        self.cards = []
        self.opened_lines = 0

    def add_card(self, card):
        self.cards.append(card)

    def display(self):
        html = ""
        for i, card in zip(range(len(self.cards)), self.cards):
            if i % 4 == 0:
                html += self.open_line()
            html += card
            if i % 4 == 3:
                html += self.close_line()
        self.close_line()
        return html

    def open_line(self):
        self.opened_lines += 1
        return '<div class="galerie">'

    def close_line(self):
        if self.opened_lines > 0:
            self.opened_lines -= 1
            return '</div>'

        return ""

def generate_html_with_all_cards():
    gallery_html = read_content("view/gallery.html")
    galerie = Galerie()
    for card in get_all_cards():
        galerie.add_card(generate_card(card))

    return re.sub("python-galerie", galerie.display(), gallery_html)

def read_content(file):
    with open(file, "r") as fh:
        return fh.read()

def write_in_file(file, html):
    with open(file, "w") as fh:
        fh.write(html)


main()
