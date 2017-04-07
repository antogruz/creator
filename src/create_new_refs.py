from cards import get_all_cards
from card_generator import generate_card

def main():
    for card in get_all_cards():
        export_ref(card.name, generate_card(card))

def export_ref(filename, card):
    dir = "src/references/"
    with open(dir + filename, "w") as fh:
        fh.write(card)


main()
