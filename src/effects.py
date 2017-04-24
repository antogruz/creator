import html
from objects import Coins

def generate_effects(effects, background_color):
    symbols_to_draw = []
    for key, value in effects.items():
        append_symbols(symbols_to_draw, key, value, background_color)

    return draw_symbols(symbols_to_draw)


def draw_symbols(symbols):
    left = get_left_position(symbols)
    draw = ""
    padding = 5
    for symbol in symbols:
        position = ["position:absolute", "top:10px", "left:{}px".format(left)]
        draw += html.add_style(position + html.size(symbol.width(), symbol.height()), symbol.get())
        left += padding + symbol.width()

    return draw

def get_left_position(symbols):
    if len(symbols) == 1:
        return 90
    else:
        return 60

def append_symbols(list, label, value, background_color):
    if label == "victory":
        list.append(Victory(value, background_color))
    if label == "coin":
        list.append(Coins(value, 50))
    if label == "bouclier":
        list.append(Bouclier())
    if label == "roue":
        list.append(Roue())
    if label == "resource":
        for resource in value:
            list.append(Resource(resource))


class Victory:
    def __init__(self, points, background_color):
        self.points = points
        if background_color == "blanche":
            self.text_color = "black-text"
        else:
            self.text_color = "white-text"

    def width(self):
        return 60

    def height(self):
        return 55

    def get(self):
        return '<img class="full-screen" src="images/laurier3.png">' + html.wrap('<div class="center {} chiffres">'.format(self.text_color), str(self.points))

class Bouclier:
    def width(self):
        return 50

    def height(self):
        return 50

    def get(self):
        return '<img class="full-screen" src="images/bouclier.png">'

class Roue:
    def width(self):
        return 50

    def height(self):
        return 51

    def get(self):
        return '<img class="full-screen" src="images/roue.png">'

class Resource:
    def __init__(self, resource):
        self.resource = resource

    def width(self):
        return 50

    def height(self):
        return 51

    def get(self):
        return '<img class="full-screen" src="images/{}.png">'.format(self.resource)
