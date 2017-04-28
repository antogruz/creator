class Card():
    def __init__(self, color, name, picture):
        self.color = color
        self.cost = []
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
    cards.append(cavite())
    cards.append(sappho())
    cards.append(scierie())
    cards.append(atelier_de_siege())

    return cards

def aqueduc():
    card = Card("bleue", "AQUEDUC", "aqueduc.png")
    card.cost.append(["pierre", "pierre", "pierre"])
    card.cost.append(["BAINS"])
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
    card.cost.append(["minerai"])
    card.players = 3
    card.effect["bouclier"] = 1
    return card

def atelier():
    card = Card("vert", "ATELIER", "atelier.jpg")
    card.cost.append(["verre"])
    card.players = 3
    card.effect["roue"] = 1
    return card

def palace():
    card = Card("bleue", "PALACE", "palace.jpg")
    card.cost.append(["pierre", "minerai", "argile", "bois", "verre", "tissu", "papyrus"])
    card.players = 7
    card.effect["victory"] = 8
    return card

def cavite():
    card = Card("marron", "CAVITÉ", "cavite.jpg")
    card.players = 3
    card.effect["resource"] = ["pierre"]
    return card

def sappho():
    card = Card("blanche", "SAPPHO", "sappho.jpg")
    card.cost.append(["coin1"])
    card.effect["victory"] = 2
    return card

def scierie():
    card = Card("marron", "SCIERIE", "scierie.jpg")
    card.cost.append(["coin1"])
    card.effect["resource"] = ["bois", "bois"]
    card.players = 4
    return card

def atelier_de_siege():
    card = Card("rouge", "ATELIER DE SIÈGE", "atelier_de_siege.jpg")
    card.cost.append(["argile", "argile", "argile", "bois"])
    card.cost.append(["LABORATOIRE"])
    card.effect["bouclier"] = 3
    return card

