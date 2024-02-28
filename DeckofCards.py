import random

class Card
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Deck:
    def __init__(self):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.reset()
        
    def reset(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
    
    def