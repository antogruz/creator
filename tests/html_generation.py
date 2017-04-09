from unittests import Tester
from card_generator import generate_card
import cards

def main():
    t = CardsGeneratorTester()
    t.runTests()


class CardsGeneratorTester(Tester):
    def aqueduc_test(self):
        confront_reference(cards.aqueduc())

    def taverne_test(self):
        confront_reference(cards.taverne())

    def caserne_test(self):
        confront_reference(cards.caserne())

    def palace_test(self):
        confront_reference(cards.palace())


def read_file_content(filename):
    with open(filename, "r") as fh:
        return fh.read()


def confront_reference(card):
    expected = read_file_content("tests/references/{}".format(card.name))
    actual = generate_card(card)
    assert_html_equals(expected, actual)


def assert_html_equals(expected, actual):
    if not expected == actual:
        print (actual)
        assert False


main()
