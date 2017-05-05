import html
from objects import BasicObject, Coins, Resource
import re
from disposition import create_line, center

def create_costs_area(cost_configs):
    return create_line([Cost(config) for config in cost_configs], padding=5, centered=False)

class Cost:
    def __init__(self, cost):
        self.padding_top = 3
        self.padding_bot = 4
        self.elements = [create_element(c) for c in cost]

    def width(self):
        return max([e.width() for e in self.elements])

    def height(self):
        return self.padding_top + sum([e.height() for e in self.elements]) + self.padding_bot

    def get(self, top, left):
        result = ""
        result += generate_banner(top, center(left, left + self.width(), 13), self.height())
        cur_top = top + self.padding_top
        for e in self.elements:
            result += e.get(cur_top, center(left, left + self.width(), e.width()))
            cur_top += e.height()

        return result

def create_element(name):
    if is_resource(name):
        return BasicObject(Resource(name, 24))
    elif "coin" in name:
        return BasicObject(Coins(re.sub("[^0-9]*", "", name), 24))
    else:
        return Dependency(name)

def is_resource(name):
    return name in ["pierre", "bois", "minerai", "argile", "verre", "papyrus", "tissu"]

class Dependency:
    def __init__(self, name):
        self.name = name

    def width(self):
        return 12

    def height(self):
        return 5 * len(self.name)

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(12, 5 * len(self.name))
        return html.add_style(position + size, dependency_text(self.name))

def dependency_text(text):
    return html.wrap('<div class="text-dependance">', text)

def generate_banner(top, left, height):
    position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
    size = html.size(13, height)
    return html.add_style(position + size, banner())

def banner():
    return '<div class="background-banner background-full"> </div>'

