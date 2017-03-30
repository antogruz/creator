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
        position = ["position:absolute", "top:{}px".format(top), "left:5px"]
        output += generate_resource(position, resource_name)
        top += between_resources
    return output

def generate_banner(height):
    position = ["position:absolute", "top:0px", "left:10px"]
    size = html.size(13, height)
    return html.add_style(position + size, banner())

def generate_resource(position, name):
    size = html.size(24, 24)
    return html.add_style(position + size, resource(name))

def banner():
    return '<div class="background-banner background-full"> </div>'

def resource(name):
    return '<img class="full-screen" src="images/{}.png"/>'.format(name)

