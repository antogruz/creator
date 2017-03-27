from unittests import Tester
from card_generator import generate_card
import cards

class CardsGeneratorTester(Tester):
    def aqueduc_test(self):
        expected = read_file_content("scripts/references/AQUEDUC")
        actual = generate_card(cards.aqueduc())
        if not expected == actual:
            print(actual)
            assert False

    def taverne_test(self):
        expected = read_file_content("scripts/references/TAVERNE")
        actual = generate_card(cards.taverne())
        if not expected == actual:
            print(actual)
            assert False


def main():
    t = CardsGeneratorTester()
    t.runTests()

def read_file_content(filename):
    with open(filename, "r") as fh:
        return fh.read()

main()
