#!/usr/bin/env python
# coding: utf8

import urllib
import list_of_cards

website = "http://loopinghpf.net/sevenwonders/resources/img/"

def main():
    for card in list_of_cards.get_all():
        download(card + ".jpg", "cards")

def download(file, destination):
    print(file)
    urllib.urlretrieve(website + file, destination + "/" + file)

main()
