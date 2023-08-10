from card import Card

# variable for the round
# variable for the done rounds
class Deck():

    self.types = []
    self.values = [6, 7, 8, 9, 10, "Jack", "Queen","King"]

    # generates the deck
    def __init__(self):
        self.deck = []
        for type in types:
            for value in values:
                card = Card(type, value)
                self.deck.append(card)


    def reveal_trump(self):
        return self.deck.pop(-1)

    def randomize(self):

