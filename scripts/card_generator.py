from cost import generate_cost
from html import *

def generate_card(config):
    return format(wrap_in_card_container(get_card_content(config)))

def wrap_in_card_container(content):
    return wrap_in_div('<div class="marge carte-size">', content)

def get_card_content(config):
    content = generate_cost(config.cost)
    content += get_dependency(config.dependency)
    content += get_effect(config.effect)
    content += get_name(config.name)
    content += get_picture(config.picture)
    content += get_players(config.players)

    return wrap_in_div('<div class="carte {}">'.format(config.color), content)

def at_position(top, left, width, height, content):
    return wrap_in_div(position(top, left, width, height), content)

def get_dependency(name):
    if not name or len(name) == 0:
        return ""

    return wrap_in_div(position(0, 32, 12, 25), wrap_in_div('<div class="background-banner background-full text-dependance">', name))

def get_effect(effects):
    html = ""
    for key, value in effects.items():
        html += create_effect(key, value)
    return html

def create_effect(label, value):
    if label == "victory":
        return victory(value)
    if label == "coin":
        return coin(value)
    return ""

def victory(n):
    content = '<img class="full-screen" src="images/laurier3.png">' + wrap_in_div('<div class="center victoire chiffres">', str(n))
    return wrap_in_div(position(10, 90, 60, 55), content)

def coin(n):
    content = '<img class="full-screen" src="images/coin.png">' + wrap_in_div('<div class="center coins chiffres">', str(n))
    return wrap_in_div(position(10, 90, 55, 55), content)

def get_name(card_name):
    name = wrap_in_div('<div class="background-name background-full text-name">', card_name)
    return wrap_in_div('<div style="position:absolute;bottom:0;left:10px;width:20px;height:90px">', name)

def get_picture(file_name):
    return wrap_in_div('<div style="position:absolute;bottom:0;right:0;height:77%;width:82%">', '<img class="full-screen" src="images/{}"/>'.format(file_name))

def get_players(n):
    return wrap_in_div(div([style(["position:absolute", dim("bottom", 3), dim("left", 50, "%")]), 'class="text-nombreJoueurs"']), "{}+".format(str(n)))

