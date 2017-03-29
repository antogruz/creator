def wrap(div, content):
    return div + content + "</div>"

def size(width, height):
    return [dim("width", width), dim("height", height)]

def position(top, left, width, height):
    return div([style(["position:absolute", dim("top", top), dim("left", left), dim("width", width), dim("height", height)])])

def div(attributes):
    return "<div " + " ".join(attributes) + ">"

def style(elements):
    return 'style="' + ";".join(elements) + '"'

def dim(label, value, unit="px"):
    return "{}:{}{}".format(label, value, unit)

def add_style(style_attributes, content):
    return wrap(div([style(style_attributes)]), content)

import re
def format(html):
    nice = ""
    pattern_open = "<\w*\s+[^>]*\s*>"
    pattern_close = "</\w*>"
    pattern = "({}|{})".format(pattern_open, pattern_close)
    divs = re.split(pattern, html)
    divs = [re.sub("\n", "", d) for d in divs]
    divs = [ d for d in divs if re.search("[^\s]", d)]
    divs = [re.sub("^\s*|\s*$", "", d) for d in divs]
    indentations = 0
    for d in divs:
        if is_close(d):
            indentations -= 1
        nice += indent(d, indentations) + "\n"
        if is_open(d):
            indentations += 1

    return nice

def is_open(div):
    return "<div" in div

def is_close(div):
    return "</" in div

def indent(text, levels):
    indentation = ""
    for i in range(levels):
        indentation += "    "
    return indentation + text


