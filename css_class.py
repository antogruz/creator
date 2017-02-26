class CssClass:
    def __init__(self, name):
        self.name = name
        self.properties = {}

    def add_property(self, key, value):
        self.properties[key] = value

    def get_css(self):
        css = ".{} {{\n".format(self.name)
        for key, value in self.properties.items():
            css += "\t {}: {};\n".format(key, value)
        css += "}\n"
        return css

