import html

def generate_dependency(name):
    if not name or len(name) == 0:
        return ""

    position = ["position:absolute", "top:0px", "left:32px"]
    size = html.size(12, 25)
    return html.add_style(position + size, create_text_on_banner(name))

def create_text_on_banner(text):
    return html.wrap('<div class="background-banner background-full text-dependance">', text)
