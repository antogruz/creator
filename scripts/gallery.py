class Gallery:
    def __init__(self, cards_per_line = 4):
        self.cards = []
        self.opened_lines = 0
        self.cards_per_line = cards_per_line

    def add_card(self, card):
        self.cards.append(card)

    def display(self):
        html = ""
        for i, card in zip(range(len(self.cards)), self.cards):
            if self.first_in_line(i):
                html += self.open_line()
            html += card
            if self.last_in_line(i):
                html += self.close_line()
        self.close_line()
        return html

    def open_line(self):
        self.opened_lines += 1
        return '<div class="galerie">'

    def close_line(self):
        if self.opened_lines > 0:
            self.opened_lines -= 1
            return '</div>'

        return ""

    def first_in_line(self, imageRank):
        return imageRank % self.cards_per_line == 0

    def last_in_line(self, imageRank):
        return imageRank % self.cards_per_line == self.cards_per_line - 1

