import html

def generate_cost(cost):
    if not cost or len(cost) == 0:
        return ""

    resources_start = 3
    between_resources = 25
    banner_height = resources_start + len(cost) * between_resources + 4
    output = generate_banner(banner_height)
    top = resources_start
    for resource_name in cost:
        size = 24
        output += html.wrap(html.position(top, 5, size, size), resource(resource_name))
        top += between_resources
    return output

def generate_banner(height):
    position = ["position:absolute", "top:0px", "left:10px"]
    size = html.size(13, height)
    return html.add_style(position + size, banner())

def banner():
    return '<div class="background-banner background-full"> </div>'

def resource(name):
    return '<img class="full-screen" src="images/{}.png"/>'.format(name)

