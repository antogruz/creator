#!/usr/bin/env python3
# coding: utf8

import crop
import os
import argparse

quad_side = 116

resources = {"Bassin argileux":"argile", "Cavité":"pierre", "Chantier":"bois", "Filon":"minerai", "Métier à tisser":"tissu", "Presse":"papyrus", "Verrerie":"verre"}

def main():
    (source, destination) = parse_source_and_destination()
    for card, resource in resources.items():
        path_to_card = source + "/" + card + ".jpg"
        path_to_resource = destination + "/" + resource + ".png"
        extract_resource(path_to_card, path_to_resource)

def extract_resource(input, output):
    crop_resource_zone(input, output)
    keep_circle(output)
    os.system("eog {}".format(output))

def crop_resource_zone(card, output):
    if "Cavité" in card:
        w = 187
        h = 38
    elif "Chantier" in card:
        w = 196
        h = 47
    elif "Verrerie" in card:
        w = 198
        h = 40
    else:
        w = 196
        h = 44
    crop.crop_quad(card, output, w, h, quad_side)

def parse_source_and_destination():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()
    return (args.source, args.destination)

def keep_circle(picture):
    os.system('convert {background} {overlay} -alpha Off -compose CopyOpacity -composite {background}'.format(overlay=create_circle(), background=picture))

def create_circle():
    filename = "tmp_circle.jpg"
    os.system('convert -size {side}x{side} xc:black -fill white -draw "circle {center},{center} 0,{center}" {file}'.format(side=quad_side, file=filename, center=quad_side/2))
    return filename

if __name__ == "__main__":
    main()
