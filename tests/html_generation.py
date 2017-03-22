from unittests import Tester
from card_generator import generate_card, Config

class CardsGeneratorTester(Tester):
    def aqueduc_test(self):
        expected = """<div class="marge carte-size">
    <div class="carte bleue">
        <div style="position:absolute;top:0px;left:10px;width:13px;height:82px">
            <div class="background-banner background-full">
            </div>
        </div>
        <div style="position:absolute;top:3px;left:5px;width:24px;height:24px">
            <img class="full-screen" src="images/pierre.png"/>
        </div>
        <div style="position:absolute;top:28px;left:5px;width:24px;height:24px">
            <img class="full-screen" src="images/pierre.png"/>
        </div>
        <div style="position:absolute;top:53px;left:5px;width:24px;height:24px">
            <img class="full-screen" src="images/pierre.png"/>
        </div>
        <div style="position:absolute;top:0px;left:32px;width:12px;height:25px">
            <div class="background-banner background-full text-dependance">
                BAINS
            </div>
        </div>
        <div style="position:absolute;top:10px;left:90px;width:60px;height:55px">
            <img class="full-screen" src="images/laurier3.png">
            <div class="center victoire chiffres">
                5
            </div>
        </div>
        <div style="position:absolute;bottom:0;left:10px;width:20px;height:90px">
            <div class="background-name background-full text-name">
                AQUEDUC
            </div>
        </div>
        <div style="position:absolute;bottom:0;right:0;height:77%;width:82%">
            <img class="full-screen" src="images/aqueduc.png"/>
        </div>
        <div style="position:absolute;bottom:3px;left:50%" class="text-nombreJoueurs">
            3+
        </div>
    </div>
</div>
"""
        actual = generate_card(Config())
        if not expected == actual:
            print(actual)
            assert False

    def taverne_test(self):
        expected = """<div class="marge carte-size">
    <div class="carte jaune">
        <div style="position:absolute;top:10px;left:90px;width:55px;height:55px">
            <img class="full-screen" src="images/coin.png">
            <div class="center coins chiffres">
                5
            </div>
        </div>
        <div style="position:absolute;bottom:0;left:10px;width:20px;height:90px">
            <div class="background-name background-full text-name">
                TAVERNE
            </div>
        </div>
        <div style="position:absolute;bottom:0;right:0;height:77%;width:82%">
            <img class="full-screen" src="images/image_taverne.jpg"/>
        </div>
        <div style="position:absolute;bottom:3px;left:50%" class="text-nombreJoueurs">
            5+
        </div>
    </div>
</div>
"""
        config = Config()
        config.color = "jaune"
        config.cost = None
        config.dependency = None
        config.name = "TAVERNE"
        config.picture = "image_taverne.jpg"
        config.players = 5
        config.effect = {"coin":5}
        actual = generate_card(config)
        if not expected == actual:
            print(actual)
            assert False



def main():
    t = CardsGeneratorTester()
    t.runTests()

main()
