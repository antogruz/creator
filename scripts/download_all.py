#!/usr/bin/env python
# coding: utf8

import urllib
import list_of_cards
import os
import argparse

website = "http://loopinghpf.net/sevenwonders/resources/img/"

def main():
    destination_dir = parse_destination_dir()
    ensure_dir_exists(destination_dir)
    for card in list_of_cards.get_all():
        print(card)
        download(card + ".jpg", destination_dir)

def parse_destination_dir():
    parser = argparse.ArgumentParser()
    parser.add_argument("destination_dir")
    return parser.parse_args().destination_dir

def ensure_dir_exists(d):
    os.system("mkdir -p {}".format(d))

def download(file, destination):
    urllib.urlretrieve(website + file, destination + "/" + file)

main()
