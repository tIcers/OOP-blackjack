import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True  # frag for later while loop


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


# test
# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()  # initialize class # define player
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(f"test player value:{test_player.value}")


# we need to keep track of a Player's starting chips, bets, and ongoing winnings
def dealer_busts(dealer, chips):
    print("Dealer bustsQ")
    chips.win_bet()  # it is came from player class


class Chips:
    def __init__(self):
        self.total = 100  # could be set to default value by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(chips):

        while True:
            try:
                chips.bet = int(input("How many chips do you want to bet?: "))

            # possibility that user do not want to give chips
            except ValueError:
                print("Please provide integer number")

            else:
                # check if user actually can bet
                if chips.bet > chips.total:
                    print(
                        f"You can not bet because the amount of bet is greater than your total chips\n YOur tips:{chips.total}")
                else:
                    break

    def hit(deck, hand):
        single_card = deck.deal()
        hand.add_card(single_card)
        hand.adjust_for_ace()

    def hit_or_stand(deck, hand):
        global playing  # i know it is bad...
        while True:
            x = input("Hit or stand? Enter H or S: ").lower()
            if x == 'h':
                deck.hit(deck, hand)
            elif x == 's':
                playing = False

            else:
                print("Please try agian.")
                continue
            break

    def show_some_card(player, dealer):
        # show only one of the dealer's card
        print("\n Dealer's Hand: ")
        print("...Card hidden...")
        print('', dealer.card[1])

        # show all card for player
        print("Player's Hand:")
        for card in player.cards:
            print(card)

    def show_all(player, dealer):

        # show all  cards for dealer

        print("Dealer's Hand:")
        for card in dealer.cards:
            print(card)
        print("Dealer's Hand =", dealer.value)

        # show all plyaer's card

        for card in player.cards:
            print(card)
        print("Player's Hand ", player.value)

    # make end game situation
    def player_busts(player, dealer, chips):
        print("Player busts!")
        chips.lose_bet()

    def player_wins(player, dealer, chips):
        print("Player win@")
        chips.win_bet()

    def dealer_busts(player, dealer, chips):
        print("Dealer busts!")
        chips.win_bet()

    def dealer_wins(player, dealer, chips):
        print("Dealer wins!")
        chips.lose_bet()

    def push(player, dealer):
        print("Dealer and Player tie! It's a push.")


# make game logic

while True:
    print("Welcome to black jack game")

    #set up settings

    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    # add card to player
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # dealer turn
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up chips for player
    # inisilize class
    player_chips = Chips()

    # ask user for bet
    take_bet(player_chips)

    #show card
    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break # lost
    if player_hand.value <=21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print(f'Player chips total: {player_chips}')

    new_game= input("Wanna play again? Y or N: ").upper()
    if new_game =="Y":
        playing = True
        continue
    else:
        print( "Thank you for playing")
