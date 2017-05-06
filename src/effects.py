import html
import re
from objects import BasicObject, Coins, Victory, Bouclier, Roue, Resource
from disposition import create_line

def generate_effects(effects, background_color):
    symbols = []
    for name in effects:
        symbols.append(create_symbol(name, background_color))

    return create_line(symbols, padding=5)

def create_symbol(name, background_color):
    if "victory" in name:
        return BasicObject(Victory(get_value(name), background_color))
    if "coin" in name:
        return BasicObject(Coins(get_value(name), 50))
    if name == "bouclier":
        return BasicObject(Bouclier())
    if name == "roue":
        return BasicObject(Roue())
    if is_resource(name):
        return BasicObject(Resource(name))

def get_value(name):
    return re.sub("[^0-9]*", "", name)

def is_resource(name):
    return name in ["pierre", "bois", "minerai", "argile", "verre", "papyrus", "tissu"]

