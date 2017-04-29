class Line:
    def __init__(self, elements, padding):
        self.elements = elements
        self.padding = padding

    def get(self, top, left):
        result = ""
        current_left = left
        for e in self.elements:
            top_position = center(top, top + self.height(), e.height())
            result += e.get(top_position, current_left)
            current_left += self.padding + e.width()
        return result

    def height(self):
        return max([e.height() for e in self.elements])

    def width(self):
        return sum([e.width() for e in self.elements]) + sum([self.padding for i in range(1, len(self.elements))])

def center(begin, end, size):
    empty_space = end - begin - size
    return empty_space / 2 + begin

class Column:
    def __init__(self, elements, padding):
        self.elements = elements
        self.padding = padding

    def get(self, top, left):
        result = ""
        current_top = top
        for e in self.elements:
            result += e.get(current_top, left)
            current_top += self.padding + e.height()
        return result
