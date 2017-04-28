import html
from objects import Coins, Resource
import re

def generate_cost(costs):
    zone = Zone()
    for cost in costs:
        zone.append(Cost(cost))

    return zone

class Zone:
    def __init__(self):
        self.costs = []
        self.padding = 5

    def append(self, cost):
        self.costs.append(cost)

    def width(self):
        return sum([c.width() + self.padding for c in self.costs])

    def height(self):
        return max([c.height() for c in self.costs])

    def get(self, top, left):
        result = ""
        cur_left = left
        for cost in self.costs:
            result += cost.get(top, cur_left)
            cur_left += cost.width() + self.padding
        return result

def center_zone(zone_left, zone_right, width):
    space = zone_right - zone_left
    return (space - width) / 2 + zone_left

class Cost:
    def __init__(self, cost):
        self.padding_top = 3
        self.padding_bot = 4
        self.elements = []
        for element in cost:
            self.elements.append(create_element(element))

    def width(self):
        return max([e.width() for e in self.elements])

    def height(self):
        return self.padding_top + sum([e.height() for e in self.elements]) + self.padding_bot

    def get(self, top, left):
        result = ""
        result += generate_banner(top, center_zone(left, left + self.width(), 13), self.height())
        cur_top = top + self.padding_top
        for e in self.elements:
            result += e.get(cur_top, center_zone(left, left + self.width(), e.width()))
            cur_top += e.height()

        return result

def create_element(name):
    if is_resource(name):
        return Resource(name, 24)
    elif "coin" in name:
        return Coins(re.sub("[^0-9]*", "", name), 24)
    else:
        return Dependency(name)

def is_resource(name):
    return name in ["pierre", "bois", "minerai", "argile", "verre", "papyrus", "tissu"]

class Dependency:
    def __init__(self, name):
        self.name = name

    def width(self):
        if not self.name or len(self.name) == 0:
            return 0
        else:
            return 12

    def height(self):
        return 5 * len(self.name)

    def get(self, top, left):
        if not self.name:
            return ""
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

