class Gallery:
    def __init__(self):
        self.cards = []
        self.opened_lines = 0

    def add_card(self, card):
        self.cards.append(card)

    def display(self):
        html = ""
        for i, card in zip(range(len(self.cards)), self.cards):
            if i % 4 == 0:
                html += self.open_line()
            html += card
            if i % 4 == 3:
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
