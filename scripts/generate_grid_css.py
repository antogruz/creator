import argparse

from css_class import CssClass
from generate_grid_html import generate_grid_html

height = 350.0
width = 227.0
cssfile = "view/css/grid.css"
htmlfile = "view/grid.html"

def main():
    columns = get_columns_count()
    lines = int(height * columns / width) + 1
    grid_css = generate_grid_css(lines, columns)
    create_file(cssfile, grid_css)
    grid_html = '<div class="marge carte-size">'
    grid_html += generate_grid_html(lines, columns)
    grid_html += '</div>'
    create_file(htmlfile, grid_html)

def get_columns_count():
    parser = argparse.ArgumentParser()
    parser.add_argument("columns", type=int)
    return parser.parse_args().columns

def generate_grid_css(lines, columns):
    return generate_all_lines(lines)
    + generate_all_columns(columns)
    + generate_all_heights(lines)
    + generate_all_widths(columns)

def generate_all_lines(count):
    return generate_all(count, generate_line)

def generate_line(line_number, lines_count):
    css_class = CssClass("line-{}".format(line_number))
    css_class.add_property("top", "{}%".format(get_percentage(line_number, lines_count)))
    css_class.add_property("position", "relative")
    css_class.add_property("display", "inline-block")
    return css_class.get_css()

def generate_all_columns(count):
    return generate_all(count, generate_column)

def generate_column(column_index, columns_count):
    css_class = CssClass("column-{}".format(column_index))
    css_class.add_property("left", "{}%".format(get_percentage(column_index, columns_count)))
    css_class.add_property("position", "relative")
    return css_class.get_css()

def generate_all_heights(count):
    return generate_all(count, generate_height)

def generate_height(index, lines_count):
    css_class = CssClass("h-{}".format(index + 1))
    css_class.add_property("height", "{}%".format(get_percentage(index + 1, lines_count)))
    return css_class.get_css()

def generate_all_widths(count):
    return generate_all(count, generate_width)

def generate_width(index, columns_count):
    css_class = CssClass("w-{}".format(index + 1))
    css_class.add_property("width", "{}%".format(get_percentage(index + 1, columns_count)))
    return css_class.get_css()

def generate_all(count, generator):
    accumulated = ""
    for i in range(count):
        accumulated += generator(i, count) + "\n"
    return accumulated

def get_percentage(dividende, divisor):
    return dividende * 100.0 / divisor

def create_file(filename, content):
    with open(filename, "w") as fh:
        fh.write(content)

main()
