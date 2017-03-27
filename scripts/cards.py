class Card():
    def __init__(self):
        self.color = None
        self.cost = None
        self.dependency = None
        self.name = None
        self.picture = None
        self.players = None
        self.effect = {}

def get_all_cards():
    cards = []
    cards.append(aqueduc())
    cards.append(taverne())

def aqueduc():
    card = Card()
    card.color = "bleue"
    card.cost = ["pierre", "pierre", "pierre"]
    card.dependency = "BAINS"
    card.name = "AQUEDUC"
    card.picture = "aqueduc.png"
    card.players = 3
    card.effect["victory"] = 5
    return card

def taverne():
    card = Card()
    card.color = "jaune"
    card.name = "TAVERNE"
    card.picture = "image_taverne.jpg"
    card.players = 5
    card.effect["coin"] = 5
    return card

