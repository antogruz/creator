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
    cards.append(caserne())
    cards.append(palace())
    cards.append(palissade())

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

def caserne():
    card = Card("rouge", "CASERNE", "caserne.jpg")
    card.cost = ["minerai"]
    card.players = 3
    card.effect["bouclier"] = 1
    return card

def atelier():
    card = Card("vert", "ATELIER", "atelier.jpg")
    card.cost = ["verre"]
    card.players = 3
    card.effect["roue"] = 1
    return card

def palace():
    card = Card("bleue", "PALACE", "palace.jpg")
    card.cost = ["pierre", "minerai", "argile", "bois", "verre", "tissu", "papyrus"]
    card.players = 7
    card.effect["victory"] = 8
    return card

def palissade():
    card = Card("rouge", "PALISSADE", "palissade.jpg")
    card.cost = ["bois"]
    card.players = 3
    card.effect["bouclier"] = 1
    return card

