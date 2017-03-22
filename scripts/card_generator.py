class Config():
    def __init__(self):
        self.color = "bleue"
        self.cost = ["pierre", "pierre", "pierre"]
        self.dependency = "BAINS"
        self.name = "AQUEDUC"
        self.picture = "aqueduc.png"
        self.players = 3
        self.effect = {"victory": 5}


def generate_card(config):
    return format(wrap_in_card_container(get_card_content(config)))

def wrap_in_card_container(content):
    return wrap_in_div('<div class="marge carte-size">', content)

def get_card_content(config):
    return wrap_in_div('<div class="carte {}">'.format(config.color), get_cost(config.cost) + get_dependency(config.dependency) + get_effect(config.effect) + get_name(config.name) + get_picture(config.picture) + get_players(config.players))

def get_cost(cost):
    if not cost or len(cost) == 0:
        return ""

    html = wrap_in_div(position(0, 10, 13, 82), '<div class="background-banner background-full"> </div>')
    left = 5
    size = 24
    top = 3
    for resource_name in cost:
        resource = '<img class="full-screen" src="images/{}.png"/>'.format(resource_name)
        html += wrap_in_div(position(top, left, size, size), resource)
        top += 25
    return html

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

def wrap_in_div(div, content):
    return div + content + "</div>"

def position(top, left, width, height):
    return div([style(["position:absolute", dim("top", top), dim("left", left), dim("width", width), dim("height", height)])])

def div(attributes):
    return "<div " + " ".join(attributes) + ">"

def style(elements):
    return 'style="' + ";".join(elements) + '"'

def dim(label, value, unit="px"):
    return "{}:{}{}".format(label, value, unit)

import re
def format(html):
    nice = ""
    pattern_open = "<\w*\s+[^>]*\s*>"
    pattern_close = "</\w*>"
    pattern = "({}|{})".format(pattern_open, pattern_close)
    divs = re.split(pattern, html)
    divs = [re.sub("\n", "", d) for d in divs]
    divs = [ d for d in divs if re.search("[^\s]", d)]
    divs = [re.sub("^\s*|\s*$", "", d) for d in divs]
    indentations = 0
    for d in divs:
        if is_close(d):
            indentations -= 1
        nice += indent(d, indentations) + "\n"
        if is_open(d):
            indentations += 1

    return nice

def is_open(div):
    return "<div" in div

def is_close(div):
    return "</" in div

def indent(text, levels):
    indentation = ""
    for i in range(levels):
        indentation += "    "
    return indentation + text


