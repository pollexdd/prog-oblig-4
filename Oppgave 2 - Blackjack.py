from operator import itemgetter
import random


class card:
    def __init__(self,value,suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠'[suit]

def price(self):
    if self.cost >= 10:
        return 10
    elif self.cost == 1:
        return 11
    return self.cost

class deck:
    def __init__(self):
        self.card = []

    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(card(i, j))    

    def draw(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self, cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)
    

    



