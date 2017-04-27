import html

def generate_name(card_name):
    return Zone(card_name)

class Zone:
    def __init__(self, name):
        self.name = name

    def width(self):
        return 20

    def height(self):
        return 11 * len(self.name)

    def get(self, top, left):
        position = ["position:absolute", "top:{}px".format(top), "left:{}px".format(left)]
        size = html.size(self.width(), self.height())
        return html.add_style(position + size, create_text_on_background(self.name))

def create_text_on_background(text):
    return html.wrap('<div class="background-name background-full text-name">', text)

