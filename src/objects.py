import html

class Quad:
    def __init__(self, size):
        self.size = size

    def width(self):
        return self.size

    def height(self):
        return self.size


class Coins(Quad):
    def __init__(self, coins, size):
        Quad.__init__(self, size)
        self.coins = coins

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.width(), self.height())
        return html.add_style(position + size, '<img class="full-screen" src="images/coin.png">' + html.wrap('<div style="font-size:{}em" class="center black-text chiffres">'.format(self.getTextSize()), str(self.coins)))

    def getTextSize(self):
        return self.size * 2.2 / 50

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

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.width(), self.height())
        return html.add_style(position + size, '<img class="full-screen" src="images/laurier3.png">' + html.wrap('<div class="center {} chiffres">'.format(self.text_color), str(self.points)))

class Bouclier(Quad):
    def __init__(self, size=46):
        Quad.__init__(self, size)

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.width(), self.height())
        return html.add_style(position + size, '<img class="full-screen" src="images/bouclier.png">')

class Roue(Quad):
    def __init__(self, size=50):
        Quad.__init__(self, size)

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.width(), self.height())
        return html.add_style(position + size, '<img class="full-screen" src="images/roue.png">')

class Resource(Quad):
    def __init__(self, resource, size=50):
        Quad.__init__(self, size)
        self.resource = resource

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.width(), self.height())
        return html.add_style(position + size, '<img class="full-screen" src="images/{}.png">'.format(self.resource))
