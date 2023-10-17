import random
# Ta pati deja cits stils

# Karsu kavas no kurienes vares panemt karti


class Table():
    def __init__(self, player, dealer, deck):
        self.player = Human(player, [], 0, 1000)
        self.dealer = Dealer(dealer, [], 0)
        self.deck = Deck()


class Deck():
    def __init__(self):
        # Velak varetu uztaisit karsu klasi - (Card)
        self.deck = [{"value": 2, "name": "two", "suit": "Clubs"},
                     {"value": 3, "name": "three", "suit": "Clubs"},
                     {"value": 4, "name": "four", "suit": "Clubs"},
                     {"value": 5, "name": "five", "suit": "Clubs"},
                     {"value": 6, "name": "six", "suit": "Clubs"},
                     {"value": 7, "name": "seven", "suit": "Clubs"},
                     {"value": 8, "name": "eight", "suit": "Clubs"},
                     {"value": 9, "name": "nine", "suit": "Clubs"},
                     {"value": 10, "name": "ten", "suit": "Clubs"},
                     {"value": 10, "name": "jack", "suit": "Clubs"},
                     {"value": 10, "name": "queen", "suit": "Clubs"},
                     {"value": 10, "name": "king", "suit": "Clubs"},
                     {"value": 11, "name": "ace", "suit": "Clubs"},
                     # spades
                     {"value": 2, "name": "two", "suit": "Spades"},
                     {"value": 3, "name": "three", "suit": "Spades"},
                     {"value": 4, "name": "four", "suit": "Spades"},
                     {"value": 5, "name": "five", "suit": "Spades"},
                     {"value": 6, "name": "six", "suit": "Spades"},
                     {"value": 7, "name": "seven", "suit": "Spades"},
                     {"value": 8, "name": "eight", "suit": "Spades"},
                     {"value": 9, "name": "nine", "suit": "Spades"},
                     {"value": 10, "name": "ten", "suit": "Spades"},
                     {"value": 10, "name": "jack", "suit": "Spades"},
                     {"value": 10, "name": "queen", "suit": "Spades"},
                     {"value": 10, "name": "king", "suit": "Spades"},
                     {"value": 11, "name": "ace", "suit": "Spades"},
                     # hearts
                     {"value": 2, "name": "two", "suit": "Hearts"},
                     {"value": 3, "name": "three", "suit": "Hearts"},
                     {"value": 4, "name": "four", "suit": "Hearts"},
                     {"value": 5, "name": "five", "suit": "Hearts"},
                     {"value": 6, "name": "six", "suit": "Hearts"},
                     {"value": 7, "name": "seven", "suit": "Hearts"},
                     {"value": 8, "name": "eight", "suit": "Hearts"},
                     {"value": 9, "name": "nine", "suit": "Hearts"},
                     {"value": 10, "name": "ten", "suit": "Hearts"},
                     {"value": 10, "name": "jack", "suit": "Hearts"},
                     {"value": 10, "name": "queen", "suit": "Hearts"},
                     {"value": 10, "name": "king", "suit": "Hearts"},
                     {"value": 11, "name": "ace", "suit": "Hearts"},
                     # diamonds
                     {"value": 2, "name": "two", "suit": "Diamonds"},
                     {"value": 3, "name": "three", "suit": "Diamonds"},
                     {"value": 4, "name": "four", "suit": "Diamonds"},
                     {"value": 5, "name": "five", "suit": "Diamonds"},
                     {"value": 6, "name": "six", "suit": "Diamonds"},
                     {"value": 7, "name": "seven", "suit": "Diamonds"},
                     {"value": 8, "name": "eight", "suit": "Diamonds"},
                     {"value": 9, "name": "nine", "suit": "Diamonds"},
                     {"value": 10, "name": "ten", "suit": "Diamonds"},
                     {"value": 10, "name": "jack", "suit": "Diamonds"},
                     {"value": 10, "name": "queen", "suit": "Diamonds"},
                     {"value": 10, "name": "king", "suit": "Diamonds"},
                     {"value": 11, "name": "ace", "suit": "Diamonds"}]

        self.shufleDeck()

        def giveCard(self):
            return self.deck.pop()

        def shufleDeck(slef):
            random.shuffle(self.deck)


# Bus divas apaksklases: House, Human


class Player():
    # Klasei vajadzetu propertijus, kur glabat kartis, karsu summu
    def __init__(self, name, hand, handSum):
        self.name = name
        self.hand = hand
        self.handSum = handSum

    # Funkcijas varetu but aprekinat karsu summu
    def calculateHandSum(self):
        for x in self.hand:
            self.handSum += x
    # Uztaisism tuksu str funkciju

    def __str__(self) -> str:
        string = "{} cards: ".format(self.name)
        for x in self.hand:
            string += x + "\n"
        return string
# Mes sito dzeku kontrolesim


class Human(Player):
    def __init__(self, name, hand, handSum, funds, bet=0):
        super().__init__(name, hand, handSum)
        self.funds = funds
        self.bet = bet

    def placeBet(self, amount):
        self.funds -= amount

    def payout(self, payout):
        self.funds += payout

    # sito velak bus jaizmaina! Paslaik vajag, lai saprotu ka suds strada
    def __str__(self) -> str:
        return super().__str__()


class Dealer(Player):
    def __init__(self, name, hand, handSum):
        super().__init__(name, hand, handSum)

    # sito velak bus jaizmaina! Paslaik vajag, lai saprotu ka suds strada

    def __str__(self) -> str:
        return super().__str__()
