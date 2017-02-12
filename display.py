import argparse
import os
import re

def main():
    html = generateHtmlToDisplay()
    writeInViewFile(html)

def generateHtmlToDisplay():
    galerie = readContent("view/galerie.html")
    cards = ""
    for file in getHtmlFilesToDisplay():
        cards += readContent(file)

    return re.sub("python-cards", cards, galerie)

def getHtmlFilesToDisplay():
    parser = argparse.ArgumentParser()
    parser.add_argument("cards", nargs="+", help="The cards to display")
    args = parser.parse_args()
    return args.cards

def readContent(file):
    with open(file, "r") as fh:
        return fh.read()

def writeInViewFile(html):
    file = "view/generated_view.html"
    with open(file, "w") as fh:
        fh.write(html)
    return file

main()
