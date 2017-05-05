import html

class Quad:
    def __init__(self, size):
        self.size = size

    def width(self):
        return self.size

    def height(self):
        return self.size

class BasicObject:
    def __init__(self, simple_generator):
        self.generator = simple_generator

    def width(self):
        return self.generator.width()

    def height(self):
        return self.generator.height()

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.generator.width(), self.generator.height())
        return html.add_style(position + size, self.generator.get())


class Coins(Quad):
    def __init__(self, coins, size):
        Quad.__init__(self, size)
        self.coins = coins

    def get(self):
        return image("coin.png") + html.wrap('<div style="font-size:{}em" class="center black-text chiffres">'.format(self.getTextSize()), str(self.coins))

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

    def get(self):
        return image("laurier3.png") + html.wrap('<div class="center {} chiffres">'.format(self.text_color), str(self.points))

class Bouclier(Quad):
    def __init__(self, size=46):
        Quad.__init__(self, size)

    def get(self):
        return image("bouclier.png")

class Roue(Quad):
    def __init__(self, size=50):
        Quad.__init__(self, size)

    def get(self):
        return image("roue.png")

class Resource(Quad):
    def __init__(self, resource, size=50):
        Quad.__init__(self, size)
        self.resource = resource

    def get(self):
        return image(self.resource + ".png")


class Picture():
    def __init__(self, file, w, h):
        self.file = file
        self.w = w
        self.h = h

    def width(self):
        return self.w

    def height(self):
        return self.h

    def get(self):
        return image(self.file)

def image(file):
    return '<img class="full-screen" src="images/{}"/>'.format(file)
