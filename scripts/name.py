from html import *

def generate_name(card_name):
    name = wrap_in_div('<div class="background-name background-full text-name">', card_name)
    return wrap_in_div('<div style="position:absolute;bottom:0;left:10px;width:20px;height:90px">', name)
