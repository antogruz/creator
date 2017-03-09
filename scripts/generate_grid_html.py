def generate_grid_html(lines, columns):
    html = ""
    for line in range(lines):
        for column in range(columns):
            html += '<div class="line-{} col-{} w-1 h-1">{}-{}</div>'.format(line, column, line, column)

    return html
