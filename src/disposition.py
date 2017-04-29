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
