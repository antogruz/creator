import html
from objects import Coins, Quad, Victory, Bouclier, Roue, Resource
from disposition import create_line

def generate_effects(effects, background_color):
    symbols = []
    for key, value in effects.items():
        append_symbols(symbols, key, value, background_color)

    return create_line(symbols, padding=5)

def append_symbols(list, label, value, background_color):
    if label == "victory":
        list.append(Victory(value, background_color))
    if label == "coin":
        list.append(Coins(value, 50))
    if label == "bouclier":
        for i in range(value):
            list.append(Bouclier())
    if label == "roue":
        list.append(Roue())
    if label == "resource":
        for resource in value:
            list.append(Resource(resource))

