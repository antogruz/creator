import html
from objects import BasicObject, Coins, Resource, Dependency, Banner
import re
from disposition import create_line, create_column, center

def create_costs_area(cost_configs):
    return create_line([create_cost(config) for config in cost_configs], padding=5, centered=False)

def create_cost(config):
    return Cost([create_element(c) for c in config])

class Cost:
    def __init__(self, elements):
        self.padding_top = 3
        self.padding_bot = 4
        self.column = create_column(elements, padding=0)

    def width(self):
        return self.column.width()

    def height(self):
        return self.padding_top + self.column.height() + self.padding_bot

    def get(self, top, left):
        banner_object = BasicObject(Banner(self.height()))
        banner = banner_object.get(top, center(left, left + self.width(), 13))
        costs = self.column.get(top + self.padding_top, left)
        return banner + costs

def create_element(name):
    if is_resource(name):
        return BasicObject(Resource(name, 24))
    elif "coin" in name:
        return BasicObject(Coins(re.sub("[^0-9]*", "", name), 24))
    else:
        return BasicObject(Dependency(name))

def is_resource(name):
    return name in ["pierre", "bois", "minerai", "argile", "verre", "papyrus", "tissu"]

