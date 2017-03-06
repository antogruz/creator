from unittests import Tester
from generate_grid_html import generate_grid_html

class GridGeneratorTester(Tester):
    def simple_test(self):
        html = generate_grid_html(0, 0)
        assert html == ""


def main():
    t = GridGeneratorTester()
    t.runTests()

main()

