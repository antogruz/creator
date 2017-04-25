import html
from objects import Coins

first_resource_top = 3
between_resources = 25

def generate_cost(cost):
    return CostZone(cost)

class CostZone:
    def __init__(self, cost):
        self.cost = cost

    def width(self):
        if self.cost:
            return 24
        else:
            return 0

    def height(self):
        return banner_height(len(self.cost))

    def get(self, top, left):
        if self.cost is None:
            return ""
        cost_generator = CostGenerator(top, left)
        return cost_generator.get(self.cost)

class CostGenerator:
    def __init__(self, top, left):
        self.top = top
        self.left = left

    def get(self, cost):
        return self.generate_banner(len(cost)) + self.generate_resources(cost)

    def generate_banner(self, resources_count):
        height = first_resource_top + resources_count * between_resources + 4
        position = ["position:absolute", "top:{}px".format(self.top), "left:{}px".format(self.left)]
        size = html.size(13, height)
        return html.add_style(position + size, banner())

    def generate_resources(self, cost):
        output = ""
        top = first_resource_top + self.top
        for resource_name in cost:
            position = ["position:absolute", "top:{}px".format(top), "left:5px"]
            output += generate_resource(position, resource_name)
            top += between_resources
        return output


def banner_height(resources):
    return 3 + resources * 24 + 4

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

