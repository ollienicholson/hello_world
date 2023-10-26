import random


class Card:
    '''Represents a standard playing card.'''
    def __init__(card, suit=0, rank=2):
        card.suit = suit
        card.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    # for element of rank names is none because the index 0 is not used/lists start at index 0
    rank_names = [
        None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
        'Queen', 'King'
    ]

    def __str__(card) -> str:
        return '%s of %s' % (
            Card.rank_names[card.rank], Card.suit_names[card.suit]
        )
        # NOTE: another way to write this is:
        # return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(card, other):
        # # NOTE: option 1
        # # check the suits
        # if card.suit < other.suit:
        #     return True
        # if card.suit > other.suit:
        #     return False

        # # suits are the same... check ranks
        # return card.rank < other.rank

        # NOTE: option 2
        t1 = card.suit, card.rank
        t2 = other.suit, other.rank
        return t1 < t2

    # __lt__ is a special method that is used to compare two objects.
    # It is used by the built-in function sorted to sort a list of objects.
    # The __lt__ method for Card objects uses the suits and ranks to determine the ordering.


# card1 = Card(1, 12)

# card2 = Card(2, 13)

# print(card1)

# print(card2)

# # using < as its defined in the class
# print(card1 < card2)


class Deck:
    '''Represents a deck of cards.'''
    def __init__(deck):
        # create a new list
        deck.cards = []
        # outer loop for suit: 0 -3
        for suit in range(4):
            # inner loop for rank: 1 - 13
            for rank in range(1, 14):
                # assingn the variable to the 'Card' class
                card = Card(suit, rank)
                #  append the card to the deck
                deck.cards.append(card)

    def __str__(deck) -> str:
        res = []
        for card in deck.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(deck):
        return deck.cards.pop()

    def add_card(deck, card):
        deck.cards.append(card)

    def shuffle(deck):
        random.shuffle(deck.cards)

    def sort(deck):
        deck.cards.sort()

    def move_cards(deck, hand, num):
        for i in range(num):
            hand.add_card(deck.pop_card())


# deck = Deck()

# deck.add_card(Card(1, 1))
# deck.sort()
# print(deck)


def find_defining_class(obj, meth_name):
    #  MRO: method resolution order
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
    return None


class Hand(Deck):
    '''Represents a hand of playing cards.'''
    def __init__(hand, label=''):
        hand.cards = []
        hand.label = label


hand = Hand('new hand')

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
# print(hand)

print(find_defining_class(hand, 'shuffle'))
