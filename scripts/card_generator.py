def generate_card():
    return format(wrap_in_card_container(get_card_content()))


def wrap_in_card_container(content):
    return """
<div class="marge carte-size">
    {}
</div>""".format(content)


def get_card_content():
    return """
<div class="carte bleue">
    {}
    {}
    {}
    {}
    {}
    {}
</div>""".format(get_cost(), get_dependency(), get_effect(), get_name(), get_picture(), get_players())

def get_cost():
    return """
    <div style="position:absolute;top:0px;left:10px;width:13px;height:82px">
        <div class="background-banner background-full"> </div>
    </div>
    <div style="position:absolute;top:3px;left:5px;width:24px;height:24px">
        <img class="full-screen" src="images/pierre.png"/>
    </div>
    <div style="position:absolute;top:28px;left:5px;width:24px;height:24px">
        <img class="full-screen" src="images/pierre.png"/>
    </div>
    <div style="position:absolute;top:53px;left:5px;width:24px;height:24px">
        <img class="full-screen" src="images/pierre.png"/>
    </div>
"""

def get_dependency():
    return """
    <div style="position:absolute;top:0px;left:32px;width:12px;height:25px">
        <div class="background-banner background-full text-dependance">
        BAINS
        </div>
    </div>
"""

def get_effect():
    return """
    <div style="position:absolute;top:10px;left:90px;width:60px;height:55px">
        <img class="full-screen" src="images/laurier3.png">
        <div class="center victoire chiffres">5</div>
    </div>
"""

def get_name():
    return """
    <div style="position:absolute;bottom:0;left:10px;width:20px;height:90px">
        <div class="background-name background-full text-name">
            AQUEDUC
        </div>
    </div>
    """

def get_picture():
    return """
    <div style="position:absolute;bottom:0;right:0;height:77%;width:82%">
        <img class="full-screen" src="images/aqueduc.png"/>
    </div>
    """

def get_players():
    return """
    <div style="position:absolute;bottom:3px;left:50%" class="text-nombreJoueurs">
        3+
    </div>
    """

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


