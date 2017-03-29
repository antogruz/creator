import html

def generate_effects(effects):
    representation = ""
    for key, value in effects.items():
        representation += create_effect(key, value)
    return representation

def create_effect(label, value):
    position = ["position:absolute", "top:10px", "left:90px"]
    symbol = create_symbol_drawer(label, value)
    size = symbol.size()
    representation = symbol.get()

    return html.add_style(position + size, representation)


def create_symbol_drawer(label, value):
    if label == "victory":
        return Victory(value)
    if label == "coin":
        return Coins(value)
    if label == "bouclier":
        return Bouclier()
    return None

class Victory:
    def __init__(self, points):
        self.points = points

    def size(self):
        return html.size(60, 55)

    def get(self):
        return '<img class="full-screen" src="images/laurier3.png">' + html.wrap('<div class="center victoire chiffres">', str(self.points))

class Coins:
    def __init__(self, coins):
        self.coins = coins

    def size(self):
        return html.size(50, 51)

    def get(self):
        return '<img class="full-screen" src="images/coin.png">' + html.wrap('<div class="center coins chiffres">', str(self.coins))


class Bouclier:
    def size(self):
        return html.size(50, 51)

    def get(self):
        return '<img class="full-screen" src="images/bouclier.png">'