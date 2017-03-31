import os
import list_of_cards

def main():
    for card in list_of_cards.get_all():
        print(card)
        crop_card(card)

def crop_card(name):
    x = 107
    y = 200
    width = 373
    height = 560
    crop("cards/" + name + ".jpg", "view/images/cards_pictures/" + name + ".jpg", x, y, width, height)

def crop(src, dest, x, y, width, height):
    src = shellquote(src)
    dest = shellquote(dest)
    print(src)
    print(dest)
    os.system("convert -crop {}x{}+{}+{} {} {}".format(width, height, x, y, src, dest))

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"


main()
