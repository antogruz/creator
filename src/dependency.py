import html

def generate_dependency(name):
    return Zone(name)

class Zone:
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
        return html.add_style(position + size, create_text_on_banner(self.name))

def create_text_on_banner(text):
    return html.wrap('<div class="background-banner background-full text-dependance">', text)
