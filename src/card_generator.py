from cost import generate_cost
from name import generate_name
from effects import generate_effects
from html import add_style, wrap, format
import html

def generate_card(config):
    return format(wrap_in_card_container(get_card_content(config)))

def wrap_in_card_container(content):
    return wrap('<div class="marge carte-size">', content)

def get_card_content(config):
    card = Card(210, 329)
    card.add_zones(generate_cost(config.cost), generate_effects(config.effect, config.color), generate_name(config.name), PictureZone(config.picture))
    content = card.get()
    content += get_players(config.players)

    return wrap('<div class="carte {}">'.format(config.color), content)

class Card:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def add_zones(self, costs, effects, name, picture):
        self.costs = costs
        self.effects = effects
        self.name = name
        self.picture = picture

    def get(self):
        offsetLeft = 5
        content = self.costs.get(0, offsetLeft)
        content += self.effects.get(10, center_zone(offsetLeft + self.costs.width(), self.width, self.effects.width()))
        content += self.name.get(self.height - self.name.height(), 10)
        content += self.picture.get(self.height - self.picture.height(), self.width - self.picture.width())
        return content


def center_zone(zone_left, zone_right, width):
    space = zone_right - zone_left
    return (space - width) / 2 + zone_left

class PictureZone:
    def __init__(self, file):
        self.file = file

    def width(self):
        return 172

    def height(self):
        return 253

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.width(), self.height())
        return add_style(position + size, '<img class="full-screen" src="images/{}"/>'.format(self.file))

def get_players(n):
    if not n:
        return ""

    position = ["position:absolute", "bottom:3px", "left:50%"]
    return add_style(position, wrap('<div class="text-nombreJoueurs">', str(n) + "+"))

def test_zone(top, left):
    return add_style(["position:absolute", "top:{}px".format(top), "left:{}px".format(left), "height:20px", "width:20px"], wrap('<div class=rouge>', str(100)))
