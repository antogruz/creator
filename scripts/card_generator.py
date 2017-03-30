from cost import generate_cost
from name import generate_name
from dependency import generate_dependency
from effects import generate_effects
from html import add_style, wrap, div, style, dim, format

def generate_card(config):
    return format(wrap_in_card_container(get_card_content(config)))

def wrap_in_card_container(content):
    return wrap('<div class="marge carte-size">', content)

def get_card_content(config):
    content = generate_cost(config.cost)
    content += generate_dependency(config.dependency)
    content += generate_effects(config.effect)
    content += generate_name(config.name)
    content += get_picture(config.picture)
    content += get_players(config.players)

    return wrap('<div class="carte {}">'.format(config.color), content)


def get_picture(file_name):
    position = ["position:absolute", "bottom:0", "right:0"]
    size = ["height:77%", "width:82%"]
    return add_style(position + size, '<img class="full-screen" src="images/{}"/>'.format(file_name))

def get_players(n):
    position = ["position:absolute", "bottom:3px", "left:50%"]
    return wrap(div([style(["position:absolute", dim("bottom", 3), dim("left", 50, "%")]), 'class="text-nombreJoueurs"']), "{}+".format(str(n)))

