from cards import get_all_cards
from card_generator import generate_card
from gallery import Gallery
import re
import argparse
import os

def main():
    args = parse_args()
    html = generate_gallery(choose_cards(args), gallery_width(args))
    write_in_file("view/generated_view.html", html)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--print", action="store_true")
    return parser.parse_args()

def gallery_width(args):
    if args.print:
        return 2
    return 4

def choose_cards(args):
    if args.diff:
        return get_cards_that_differs()

    return [generate_card(card) for card in get_all_cards()]

def get_cards_that_differs():
    cards = []
    for card in get_all_cards():
        generated = generate_card(card)
        reference_file = "tests/references/{}".format(card.name)
        if os.path.exists(reference_file):
            reference = read_content(reference_file)
            if generated != reference:
                cards.append(reference)
                cards.append(generated)
    return cards

def generate_gallery(cards, width):
    gallery_html = read_content("view/gallery.html")
    gallery = Gallery(width)
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
