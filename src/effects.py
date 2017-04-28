import html
from objects import Coins, Quad, Victory, Bouclier, Roue, Resource

def generate_effects(effects, background_color):
    symbols = []
    for key, value in effects.items():
        append_symbols(symbols, key, value, background_color)

    return Zone(symbols)

padding = 5
class Zone:
    def __init__(self, symbols):
        self.symbols = symbols

    def width(self):
        width = 0
        for s in self.symbols:
            width += s.width() + padding
        return width

    def height(self):
        return 50

    def get(self, top, left):
        result = ""
        cur_left = left
        for symbol in self.symbols:
            result += symbol.get(top, cur_left)
            cur_left += symbol.width() + padding
        return result

def append_symbols(list, label, value, background_color):
    if label == "victory":
        list.append(Victory(value, background_color))
    if label == "coin":
        list.append(Coins(value, 50))
    if label == "bouclier":
        for i in range(value):
            list.append(Bouclier())
    if label == "roue":
        list.append(Roue())
    if label == "resource":
        for resource in value:
            list.append(Resource(resource))

