import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True # frag for later while loop


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} Of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):  # only for when you print class
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "THe deck has : " + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # ace has special cases, could be one or eleven so keep track

    def add_card(self, card):
        # from Deck.deal() ==> single_card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]  # check if all value is above 21 or not.
        # Add value by getting values which is associated with number(in this case value) and add it

        # track aces

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        # if the total is greater than 21 ace will be 10 and substract ace one card
        while self.value > 21 and self.aces:  # using number as an integer but truthy and falsy way
            self.value -= 10
            self.aces -= 1


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()  # initialize class # define player
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(f"test player value:{test_player.value}")
