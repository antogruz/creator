from cards import get_all_cards
from card_generator import generate_card
from gallery import Gallery
import re
import argparse

def main():
    html = generate_gallery(choose_cards())
    write_in_file("view/generated_view.html", html)

def choose_cards():
    if is_diff_mode():
        return get_cards_that_differs()
    else:
        return [generate_card(card) for card in get_all_cards()]

def is_diff_mode():
    parser = argparse.ArgumentParser()
    parser.add_argument("--diff", action="store_true")
    return parser.parse_args().diff

def get_cards_that_differs():
    cards = []
    for card in get_all_cards():
        generated = generate_card(card)
        reference = read_content("tests/references/{}".format(card.name))
        if generated != reference:
            cards.append(reference)
            cards.append(generated)
    return cards

def generate_gallery(cards):
    gallery_html = read_content("view/gallery.html")
    gallery = Gallery()
    for card in cards:
        gallery.add_card(card)

    return re.sub("python-galerie", gallery.display(), gallery_html)

def read_content(file):
    with open(file, "r") as fh:
        return fh.read()

def write_in_file(file, html):
    with open(file, "w") as fh:
        fh.write(html)

main()
