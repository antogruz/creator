from unittests import Tester, assert_equals
from disposition import Line, Column

def main():
    LineTester().runTests()
    ColumnTester().runTests()

class Element:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def width(self):
        return self.w

    def height(self):
        return self.h

    def get(self, top, left):
        return "-".join([str(top), str(left)])


class LineTester(Tester):
    def test_empty_line(self):
        line = Line([], 0)
        assert_equals("", Line([], 0).get(0, 0))

    def test_line_with_one_element(self):
        line = Line([Element(0, 0)], 0)
        assert_equals("1-2", line.get(1, 2))

    def test_line_with_several_elements(self):
        line = Line([Element(2, 3), Element(0, 0)], 5)
        assert_equals("1-0" + "1-7", line.get(1, 0))

    def test_line_dimensions(self):
        line = Line([Element(1, 2), Element(3, 1)], 99)
        assert_equals(2, line.height())
        assert_equals(99 + 1 + 3, line.width())


class ColumnTester(Tester):
    def test_empty_column(self):
        col = Column([Element(2, 3), Element(0, 0)], 5)
        assert_equals("1-0" + "9-0", col.get(1, 0))

main()
