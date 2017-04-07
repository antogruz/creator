import html

def generate_name(card_name):
    position = ["position:absolute", "bottom:0", "left:10px"]
    size = get_size(card_name)
    return html.add_style(position + size, create_text_on_background(card_name))

def create_text_on_background(text):
    return html.wrap('<div class="background-name background-full text-name">', text)

def get_size(text):
    banner_height = 11 * len(text)
    return html.size(20, banner_height)
