import html

def generate_name(card_name):
    position = ["position:absolute", "bottom:0", "left:10px"]
    banner_height = 11 * len(card_name)
    size = html.size(20, banner_height)
    name = html.wrap_in_div('<div class="background-name background-full text-name">', card_name)
    return html.wrap_in_div(html.div([html.style(position + size)]), name)
