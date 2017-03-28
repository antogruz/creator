import html

def generate_name(card_name):
    position = ["position:absolute", "bottom:0", "left:10px"]
    size = html.size(20, 90)
    name = html.wrap_in_div('<div class="background-name background-full text-name">', card_name)
    return html.wrap_in_div(html.div([html.style(position + size)]), name)
