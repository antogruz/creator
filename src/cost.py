import html
from objects import Coins

first_resource_top = 3
between_resources = 25

def generate_cost(cost):
    if not cost or len(cost) == 0:
        return ""

    return generate_banner(len(cost)) + generate_resources(cost)

def generate_banner(resources_count):
    height = first_resource_top + resources_count * between_resources + 4
    position = ["position:absolute", "top:0px", "left:10px"]
    size = html.size(13, height)
    return html.add_style(position + size, banner())

def generate_resources(cost):
    output = ""
    top = first_resource_top
    for resource_name in cost:
        position = ["position:absolute", "top:{}px".format(top), "left:5px"]
        output += generate_resource(position, resource_name)
        top += between_resources
    return output


def generate_resource(position, name):
    size = html.size(24, 24)
    return html.add_style(position + size, resource(name))

def banner():
    return '<div class="background-banner background-full"> </div>'

import re
def resource(name):
    if "coin" in name:
        return coin(re.sub("[^0-9]*", "", name))
    else:
        return '<img class="full-screen" src="images/{}.png"/>'.format(name)

def coin(n):
    c = Coins(n, 24)
    return c.get()

