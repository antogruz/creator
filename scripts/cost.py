from html import *

def generate_cost(cost):
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

