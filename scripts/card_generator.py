def generate_card():
    return format(wrap_in_card_container(get_card_content()))


def wrap_in_card_container(content):
    return """
<div class="marge carte-size">
    {}
</div>""".format(content)


def get_card_content():
    return """<div class="carte bleue">
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
        <div style="position:absolute;top:0px;left:32px;width:12px;height:25px">
            <div class="background-banner background-full text-dependance">
            BAINS
            </div>
        </div>
        <div style="position:absolute;top:10px;left:90px;width:60px;height:55px">
            <img class="full-screen" src="images/laurier3.png">
            <div class="center victoire chiffres">5</div>
        </div>
        <div style="position:absolute;bottom:0;left:10px;width:20px;height:90px">
            <div class="background-name background-full text-name">
                AQUEDUC
            </div>
        </div>
        <div style="position:absolute;bottom:0;right:0;height:77%;width:82%">
            <img class="full-screen" src="images/aqueduc.png"/>
        </div>
        <div style="position:absolute;bottom:3px;left:50%" class="text-nombreJoueurs">
            3+
        </div>
    </div>"""


import re
def format(html):
    nice = ""
    divs = re.split("(<.*>)", html)
    divs = [d for d in divs if not "\n" in d ]
    print(divs)
    indentations = 0
    for d in divs:
        nice += indent(d, indentations) + "\n"
        if is_open(d):
            indentations += 1
        if is_close(d):
            indentations -= 1

    return nice

def is_open(div):
    return "<div" in div

def is_close(div):
    return "</" in div

def indent(text, levels):
    indentation = ""
    for i in range(levels):
        indentation += "\t"
    return indentation + text


