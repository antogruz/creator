import argparse
from generate_grid_html import generate_grid_html
from generate_grid_css import generate_grid_css

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

def create_file(filename, content):
    with open(filename, "w") as fh:
        fh.write(content)

main()
