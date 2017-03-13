import argparse

from css_class import CssClass

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

