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

    def get(self):
        return '<img class="full-screen" src="images/coin.png">' + html.wrap('<div style="font-size:{}em" class="center black-text chiffres">'.format(self.getTextSize()), str(self.coins))

    def getTextSize(self):
        return self.size * 2.2 / 50
