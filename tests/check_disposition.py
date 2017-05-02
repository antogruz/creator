from unittests import Tester, assert_equals
from disposition import create_line, create_column

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
        return "-".join([str(int(top)), str(int(left))])


class LineTester(Tester):
    def test_empty_line(self):
        line = create_line([], 0)
        assert_equals("", line.get(0, 0))

    def test_line_with_one_element(self):
        line = create_line([Element(0, 0)], 0)
        assert_equals("1-2", line.get(1, 2))

    def test_line_with_several_elements_of_same_height(self):
        line = create_line([Element(2, 3), Element(0, 3)], 5)
        assert_equals("1-0" + "1-7", line.get(1, 0))

    def test_line_dimensions(self):
        line = create_line([Element(1, 2), Element(3, 1)], 99)
        assert_equals(2, line.height())
        assert_equals(99 + 1 + 3, line.width())

    def test_that_elements_of_different_heights_are_centered(self):
        line = create_line([Element(0, 1), Element(0, 3)], 0)
        assert_equals("1-0" + "0-0", line.get(0, 0))


class ColumnTester(Tester):
    def test_empty_column(self):
        col = create_column([], 0)
        assert_equals("", col.get(0, 0))

    def test_column_with_one_element(self):
        col = create_column([Element(0, 0)], 0)
        assert_equals("1-2", col.get(1, 2))

    def test_column_with_several_elements_of_same_width(self):
        col = create_column([Element(3, 2), Element(3, 1)], 5)
        assert_equals("0-1" + "7-1", col.get(0, 1))

    def test_column(self):
        col = create_column([Element(3, 4), Element(1, 1)], 5)
        assert_equals("1-0" + "10-1", col.get(1, 0))

main()
