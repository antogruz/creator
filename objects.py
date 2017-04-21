import html

class Coins:
    def __init__(self, coins, height):
        self.coins = coins
        self.height = height

    def size(self):
        return html.size(self.height, self.height)

    def get(self):
        return '<img class="full-screen" src="images/coin.png">' + html.wrap('<div style="font-size:{}em" class="center black-text chiffres">'.format(self.getTextSize()), str(self.coins))

    def getTextSize(self):
        return self.height * 2.2 / 50
