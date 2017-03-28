from html import *

def generate_name(card_name):
    position = ["position:absolute", "bottom:0", "left:10px"]
    size = ["width:20px", "height:90px"]
    name = wrap_in_div('<div class="background-name background-full text-name">', card_name)
    return wrap_in_div(div([style(position + size)]), name)
