#!/usr/bin/env python3

import os
import list_of_cards
import argparse

def main():
    (source, destination) = parse_source_and_destination()
    ensure_dir_exists(destination)
    for card in list_of_cards.get_all():
        print(card)
        crop_card(jpg_file(source, card), jpg_file(destination, card))

def parse_source_and_destination():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()
    return (args.source, args.destination)

def ensure_dir_exists(d):
    os.system("mkdir -p {}".format(d))

def crop_card(input, output):
    crop(input, output, 107, 200, 373, 560)

def crop_quad(input, output, x, y, side):
    crop(input, output, x, y, side, side)

def crop(src, dest, x, y, width, height):
    src = shellquote(src)
    dest = shellquote(dest)
    os.system("convert -crop {}x{}+{}+{} {} {}".format(width, height, x, y, src, dest))

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"

def jpg_file(dir, name):
    return dir + "/" + name + ".jpg"


if __name__ == "__main__":
    main()
