from unittests import Tester, assert_equals
from disposition import Line

def main():
    t = LineTester()
    t.runTests()

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
        line = Line([Element(2, 2), Element(0, 0)], 5)
        assert_equals("1-0" + "1-7", line.get(1, 0))


main()
