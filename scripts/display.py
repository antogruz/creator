import argparse
import re


def main():
    html = generate_html_to_display()
    write_in_view_file(html)


def generate_html_to_display():
    gallery = read_content("view/gallery.html")
    cards = ""
    for file in get_html_files_to_display():
        cards += read_content(file)

    return re.sub("python-cards", cards, gallery)


def get_html_files_to_display():
    parser = argparse.ArgumentParser()
    parser.add_argument("cards", nargs="+", help="The cards to display")
    args = parser.parse_args()
    return args.cards


def read_content(file):
    with open(file, "r") as fh:
        return fh.read()


def write_in_view_file(html):
    file = "view/generated_view.html"
    with open(file, "w") as fh:
        fh.write(html)

main()
