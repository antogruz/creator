from html import *

def generate_cost(cost):
    if not cost or len(cost) == 0:
        return ""

    resources_start = 3
    between_resources = 25
    banner_height = resources_start + len(cost) * between_resources + 4

    html = wrap_in_div(position(0, 10, 13, banner_height), banner())
    left = 5
    size = 24
    top = resources_start
    for resource_name in cost:
        html += wrap_in_div(position(top, left, size, size), resource(resource_name))
        top += between_resources
    return html

def banner():
    return '<div class="background-banner background-full"> </div>'

def resource(name):
    return '<img class="full-screen" src="images/{}.png"/>'.format(name)

