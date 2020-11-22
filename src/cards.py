class Card():
    def __init__(self, color, name, picture):
        self.color = color
        self.costs = []
        self.effects = []
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
    cards.append(parlement())
    cards.append(lou())

    return cards

def aqueduc():
    card = Card("bleue", "AQUEDUC", "aqueduc.png")
    card.costs.append(["pierre", "pierre", "pierre"])
    card.costs.append(["BAINS"])
    card.players = 3
    card.effects.append("victory5")
    return card

def taverne():
    card = Card("jaune", "TAVERNE", "image_taverne.jpg")
    card.players = 5
    card.effects.append("coin5")
    return card

def caserne():
    card = Card("rouge", "CASERNE", "caserne.jpg")
    card.costs.append(["minerai"])
    card.players = 3
    card.effects.append("bouclier")
    return card

def parlement():
    card = Card("bleue", "PARLEMENT", "palace.jpg")
    card.costs.append(["pierre", "pierre", "pierre", "minerai", "argile", "verre"])
    card.costs.append(["coins2", "PALACE"])
    card.effects.append("victory7")
    card.effects.append("coin12")
    return card

def atelier():
    card = Card("vert", "ATELIER", "atelier.jpg")
    card.costs.append(["verre"])
    card.players = 3
    card.effects.append("roue")
    return card

def palace():
    card = Card("bleue", "PALACE", "palace.jpg")
    card.costs.append(["pierre", "minerai", "argile", "bois", "verre", "tissu", "papyrus"])
    card.players = 7
    card.effects.append("victory8")
    return card

def cavite():
    card = Card("marron", "CAVITÉ", "cavite.jpg")
    card.players = 3
    card.effects.append("pierre")
    return card

def sappho():
    card = Card("blanche", "SAPPHO", "sappho.jpg")
    card.costs.append(["coin1"])
    card.effects.append("victory2")
    return card

def scierie():
    card = Card("marron", "SCIERIE", "scierie.jpg")
    card.costs.append(["coin1"])
    card.effects.append("bois")
    card.effects.append("bois")
    card.players = 4
    return card

def atelier_de_siege():
    card = Card("rouge", "ATELIER DE SIÈGE", "atelier_de_siege.jpg")
    card.costs.append(["argile", "argile", "argile", "bois"])
    card.costs.append(["LABORATOIRE"])
    card.effects.append("bouclier")
    card.effects.append("bouclier")
    card.effects.append("bouclier")
    return card

def lou():
    card = Card("blanche", "LOU", "louzoom.jpg")
    card.costs.append(["coin1"])
    card.effects.append("victory3")
    return card

