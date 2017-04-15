import html

def generate_effects(effects, background_color):
    representation = ""
    for key, value in effects.items():
        representation += create_effect(key, value, background_color)
    return representation

def create_effect(label, value, background_color):
    position = ["position:absolute", "top:10px", "left:90px"]
    symbol = create_symbol_drawer(label, value, background_color)
    size = symbol.size()
    representation = symbol.get()

    return html.add_style(position + size, representation)


def create_symbol_drawer(label, value, background_color):
    if label == "victory":
        return Victory(value, background_color)
    if label == "coin":
        return Coins(value)
    if label == "bouclier":
        return Bouclier()
    if label == "roue":
        return Roue()
    if label == "resource":
        return Resource(value)

class Victory:
    def __init__(self, points, background_color):
        self.points = points
        if background_color == "blanche":
            self.text_color = "coins"
        else:
            self.text_color = "victoire"

    def size(self):
        return html.size(60, 55)

    def get(self):
        return '<img class="full-screen" src="images/laurier3.png">' + html.wrap('<div class="center {} chiffres">'.format(self.text_color), str(self.points))

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

class Roue:
    def size(self):
        return html.size(50, 51)

    def get(self):
        return '<img class="full-screen" src="images/roue.png">'

class Resource:
    def __init__(self, resources):
        self.resources = resources

    def size(self):
        return html.size(50, 51)

    def get(self):
        return '<img class="full-screen" src="images/{}.png">'.format(self.resources[0])
