from enum import Enum

axe_x = 0
axe_y = 1

def create_line(elements, padding, centered = True):
    return Line(Horizontal(), elements, padding, centered)

def create_column(elements, padding, centered = True):
    return Line(Vertical(), elements, padding, centered)

class Horizontal():
    def get_element(self, element, x, y):
        return element.get(y, x)

    def get_xy(self, top, left):
        return (left, top)

    def get_size(self, element, axe):
        if axe == axe_x:
            return element.width()
        else:
            return element.height()

class Vertical():
    def get_element(self, element, x, y):
        return element.get(x, y)

    def get_xy(self, top, left):
        return (top, left)

    def get_size(self, element, axe):
        if axe == axe_x:
            return element.height()
        else:
            return element.width()

class Line:
    def __init__(self, direction, elements, padding, centered):
        self.elements = elements
        self.padding = padding
        self.direction = direction
        self.centered = centered

    def get(self, top, left):
        result = ""
        (x, y) = self.direction.get_xy(top, left)
        for e in self.elements:
            if self.centered:
                e_y = center(y , y + self.size(axe_y), self.direction.get_size(e, axe_y))
            else:
                e_y = y
            result += self.direction.get_element(e, x, e_y)
            x += self.padding + self.direction.get_size(e, axe_x)
        return result

    def width(self):
        return self.size(axe_x)

    def height(self):
        return self.size(axe_y)

    def size(self, axe):
        if axe == axe_x:
            return sum([self.direction.get_size(e, axe_x) for e in self.elements]) + sum([self.padding for i in range(1, len(self.elements))])
        else:
            return max([self.direction.get_size(e, axe_y) for e in self.elements])

def center(begin, end, size):
    empty_space = end - begin - size
    result = empty_space / 2 + begin
    return result

