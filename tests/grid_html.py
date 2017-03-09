from unittests import Tester
from generate_grid_html import generate_grid_html

class GridGeneratorTester(Tester):
    def empty_grids_test(self):
        assert generate_grid_html(0, 0) == ""
        assert generate_grid_html(1, 0) == ""
        assert generate_grid_html(0, 1) == ""

    def one_quad_test(self):
        assert generate_grid_html(1, 1) == '<div class="line-0 col-0 w-1 h-1">0-0</div>'

    def two_lines_test(self):
        html = generate_grid_html(2, 1)
        assert html == '<div class="line-0 col-0 w-1 h-1">0-0</div><div class="line-1 col-0 w-1 h-1">1-0</div>'

    def two_columns_test(self):
        html = generate_grid_html(1, 2)
        assert html == '<div class="line-0 col-0 w-1 h-1">0-0</div><div class="line-0 col-1 w-1 h-1">0-1</div>'


def main():
    t = GridGeneratorTester()
    t.runTests()

main()
