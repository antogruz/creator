import html
from objects import Coins

def generate_effects(effects, background_color):
    symbols_to_draw = []
    for key, value in effects.items():
        append_symbols(symbols_to_draw, key, value, background_color)

    return draw_symbols(symbols_to_draw)


def draw_symbols(list):
    symbol = list[0]
    position = ["position:absolute", "top:10px", "left:90px"]

    return html.add_style(position + symbol.size(), symbol.get())


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

    def size(self):
        return html.size(60, 55)

    def get(self):
        return '<img class="full-screen" src="images/laurier3.png">' + html.wrap('<div class="center {} chiffres">'.format(self.text_color), str(self.points))

class Bouclier:
    def size(self):
        return html.size(50, 51)

    def get(self):
        return '<img class="full-screen" src="images/bouclier.png">'

class Roue:
    def size(self):
        return html.size(50, 51)

    def get(self):
        return '<img class="full-screen" src="images/roue.png">'

class Resource:
    def __init__(self, resource):
        self.resource = resource

    def size(self):
        return html.size(50, 51)

    def get(self):
        return '<img class="full-screen" src="images/{}.png">'.format(self.resource)
