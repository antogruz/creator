def generate_card():
    return format(wrap_in_card_container(get_card_content()))

def wrap_in_card_container(content):
    return wrap_in_div('<div class="marge carte-size">', content)

def get_card_content():
    return wrap_in_div('<div class="carte bleue">', get_cost() + get_dependency() + get_effect() + get_name() + get_picture() + get_players())

def get_cost():
    pierre = '<img class="full-screen" src="images/pierre.png"/>'
    cost = ""
    cost += wrap_in_div(position(0, 10, 13, 82), '<div class="background-banner background-full"> </div>')
    size = 24
    cost += wrap_in_div(position(3, 5, size, size), pierre)
    cost += wrap_in_div(position(28, 5, size, size), pierre)
    cost += wrap_in_div(position(53, 5, size, size), pierre)
    return cost

def position(top, left, width, height):
    return '<div style="position:absolute;top:{}px;left:{}px;width:{}px;height:{}px">'.format(top, left, width, height)

def get_dependency():
    return wrap_in_div(position(0, 32, 12, 25), wrap_in_div('<div class="background-banner background-full text-dependance">', "BAINS"))

def get_effect():
    victory_points = '<img class="full-screen" src="images/laurier3.png">' + wrap_in_div('<div class="center victoire chiffres">', "5")
    return wrap_in_div(position(10, 90, 60, 55), victory_points)

def get_name():
    name = wrap_in_div('<div class="background-name background-full text-name">', "AQUEDUC")
    return wrap_in_div('<div style="position:absolute;bottom:0;left:10px;width:20px;height:90px">', name)

def get_picture():
    return wrap_in_div('<div style="position:absolute;bottom:0;right:0;height:77%;width:82%">', '<img class="full-screen" src="images/aqueduc.png"/>')

def get_players():
    return wrap_in_div('<div style="position:absolute;bottom:3px;left:50%" class="text-nombreJoueurs">', "3+")

def wrap_in_div(div, content):
    return div + content + "</div>"

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


