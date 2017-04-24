import html
from objects import Coins, Quad, Victory, Bouclier, Roue, Resource

def generate_effects(effects, background_color):
    symbols_to_draw = []
    for key, value in effects.items():
        append_symbols(symbols_to_draw, key, value, background_color)

    return draw_symbols(symbols_to_draw)


def draw_symbols(symbols):
    left = get_left_position(symbols)
    draw = ""
    padding = 5
    for symbol in symbols:
        position = ["position:absolute", "top:10px", "left:{}px".format(left)]
        draw += html.add_style(position + html.size(symbol.width(), symbol.height()), symbol.get())
        left += padding + symbol.width()

    return draw

def get_left_position(symbols):
    if len(symbols) == 1:
        return 90
    elif len(symbols) == 2:
        return 60
    else:
        return 52

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

