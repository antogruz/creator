height = 350.0
width = 227.0
cssfile = "view/css/grid.css"

def main():
    grid_css = generate_grid_css(height, width)
    create_file(cssfile, grid_css)

def generate_grid_css(height, width):
    columns = 20
    lines = int(height * columns / width) + 1
    return generate_all_lines(lines) + generate_all_columns(columns) + generate_all_heights(lines) + generate_all_widths(columns)

def generate_all_lines(count):
    return generate_all(count, generate_line)

def generate_line(line_number, lines_count):
    return create_css_class("line-{}".format(line_number), "top", "{}%".format(get_percentage(line_number, lines_count)))

def generate_all_columns(count):
    return generate_all(count, generate_column)

def generate_column(column_index, columns_count):
    return create_css_class("column-{}".format(column_index),
            "left",
            "{}%".format(get_percentage(column_index, columns_count)))

def generate_all_heights(count):
    return generate_all(count, generate_height)

def generate_height(index, lines_count):
    return create_css_class("h-{}".format(index + 1),
            "height",
            "{}%".format(get_percentage(index + 1, lines_count)))

def generate_all_widths(count):
    return generate_all(count, generate_width)

def generate_width(index, columns_count):
    return create_css_class("w-{}".format(index + 1),
            "width",
            "{}%".format(get_percentage(index + 1, columns_count)))

def generate_all(count, generator):
    accumulated = ""
    for i in range(count):
        accumulated += generator(i, count) + "\n"
    return accumulated

def get_percentage(dividende, divisor):
    return dividende * 100.0 / divisor

def create_css_class(class_name, property, value):
    return """.{} {{
    {}: {};
}}""".format(class_name, property, value)

def create_file(filename, content):
    with open(filename, "w") as fh:
        fh.write(content)

main()
