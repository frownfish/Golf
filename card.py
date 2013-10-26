class Card:
    ''' '''
    SUITS = {'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades'}
    CARD_NAMES = {'1': 'Ace', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
                  '8': '8', '9': '9', 'T': '10', 'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'W': 'Joker'}
    CARD_POINTS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 0, 'W': -2}
    def __init__(self, n, suit):
        self.n = n
        self.suit = suit
        self.up = True

    def __str__(self):
        HIDDEN = '-----------' 
        return '{0} of {1}'.format(self.CARD_NAMES[self.n], self.SUITS[self.suit]) if self.up else HIDDEN