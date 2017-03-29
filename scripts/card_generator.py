from cost import generate_cost
from name import generate_name
from dependency import generate_dependency
from html import *

def generate_card(config):
    return format(wrap_in_card_container(get_card_content(config)))

def wrap_in_card_container(content):
    return wrap('<div class="marge carte-size">', content)

def get_card_content(config):
    content = generate_cost(config.cost)
    content += generate_dependency(config.dependency)
    content += get_effect(config.effect)
    content += generate_name(config.name)
    content += get_picture(config.picture)
    content += get_players(config.players)

    return wrap('<div class="carte {}">'.format(config.color), content)


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
    if label == "bouclier":
        return bouclier(value)
    return ""

def victory(n):
    content = '<img class="full-screen" src="images/laurier3.png">' + wrap('<div class="center victoire chiffres">', str(n))
    return wrap(position(10, 90, 60, 55), content)

def coin(n):
    content = '<img class="full-screen" src="images/coin.png">' + wrap('<div class="center coins chiffres">', str(n))
    return wrap(position(10, 90, 50, 51), content)

def bouclier(n):
    content = '<img class="full-screen" src="images/bouclier.png">'
    return wrap(position(10, 90, 50, 51), content)

def get_picture(file_name):
    return wrap('<div style="position:absolute;bottom:0;right:0;height:77%;width:82%">', '<img class="full-screen" src="images/{}"/>'.format(file_name))

def get_players(n):
    return wrap(div([style(["position:absolute", dim("bottom", 3), dim("left", 50, "%")]), 'class="text-nombreJoueurs"']), "{}+".format(str(n)))

