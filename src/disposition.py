class Line:
    def __init__(self, elements, padding):
        self.elements = elements
        self.padding = padding

    def get(self, top, left):
        result = ""
        current_left = left
        for e in self.elements:
            result += e.get(top, current_left)
            current_left += self.padding + e.width()
        return result

    def height(self):
        return max([e.height() for e in self.elements])

    def width(self):
        return sum([e.width() for e in self.elements]) + sum([self.padding for i in range(1, len(self.elements))])

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
