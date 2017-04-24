import html
from objects import Coins, Quad, Victory, Bouclier, Roue, Resource

def generate_effects(effects, background_color, left):
    symbols_to_draw = []
    for key, value in effects.items():
        append_symbols(symbols_to_draw, key, value, background_color)

    return draw_symbols(symbols_to_draw, left)


padding = 5
def draw_symbols(symbols, left):
    left = get_left_position(left, 210, symbols)
    draw = ""
    for symbol in symbols:
        position = ["position:absolute", "top:10px", "left:{}px".format(left)]
        draw += html.add_style(position + html.size(symbol.width(), symbol.height()), symbol.get())
        left += padding + symbol.width()

    return draw

def get_left_position(zone_left, zone_right, symbols):
    space = zone_right - zone_left
    space_occupied = get_total_width(symbols)
    return (space - space_occupied) / 2 + zone_left

def get_total_width(symbols):
    width = 0
    for s in symbols:
        width += s.width() + padding
    return width

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

