class Card():
    def __init__(self, color, name, picture):
        self.color = color
        self.cost = None
        self.dependency = None
        self.name = name
        self.picture = picture
        self.players = None
        self.effect = {}

def get_all_cards():
    cards = []
    cards.append(aqueduc())
    cards.append(taverne())

    return cards

def aqueduc():
    card = Card("bleue", "AQUEDUC", "aqueduc.png")
    card.cost = ["pierre", "pierre", "pierre"]
    card.dependency = "BAINS"
    card.players = 3
    card.effect["victory"] = 5
    return card

def taverne():
    card = Card("jaune", "TAVERNE", "image_taverne.jpg")
    card.players = 5
    card.effect["coin"] = 5
    return card

