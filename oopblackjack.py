import random as rand
# Ta pati deja cits stils


class Table():

    """
    Table klase vajadzetu but visiem noteikumiem
    """

    def __init__(self, player, dealer):
        self.player = Human(player, [])
        self.dealer = Dealer(dealer, [])
        self.deck = Deck()
        self.dealerMove = False

        self.deal_first_hand()

    def deal_first_hand(self):
        self.player.hand.append(self.deck.giveCard())
        self.dealer.hand.append(self.deck.giveCard())
        self.player.hand.append(self.deck.giveCard())
        self.dealer.hand.append(self.deck.giveCard())

    # Izprinteju galdu jeb kartis kas atrodas uz galda un speletaju rokas summu.
    def __str__(self):
        if self.dealerMove:
            string = "{}".format(self.dealer)
            string += "\n\n\n\n\n\n"
            string += "{}".format(self.player)
            return string
        else:
            string = "{}".format(self.dealer.first_hand_print())
            string += "\n\n\n\n\n\n"
            string += "{}".format(self.player)
            return string


class Card():

    """
    Karsu klase, lai lasamak varetu savienotu kodu, jo tas es tas varetu likt
    dictionerijos. Vieglak varetu izprintet kartis,
    kartis kuras ir ar divciparu skailti tiks izprintetas nedaudz lielakas.

    Klase ir kopa ar karsu zimem.

    Klasei ir vertibas un zimes ipasibas.

    String funkcijas, kas izprinte kartis iegaumejot to vertibu un izmantojot kopu ar
    karsu zimem

    """
    suit_unicode = {
        "Diamonds": "\u2666",
        "Hearts": "\u2665",
        "Spades": "\u2660",
        "Clubs": "\u2663"
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        if self.value > 9:
            string = " ----- "
            string += "\n|{} {} |".format(self.value,
                                          self.suit_unicode[self.suit])
            string += "\n|     |"
            string += "\n|     |"
            string += "\n ----- \n"
        else:
            string = " ---- "
            string += "\n|{} {} |".format(self.value,
                                          self.suit_unicode[self.suit])
            string += "\n|    |"
            string += "\n|    |"
            string += "\n ---- \n"
        return string


class Deck():

    """
    Karsu kavas klase, kurai ipasibas bus kava un kavu samaisisanam, kur kavu uzreiz samaisis.
    Kavai kartis tiek veidotas no karsu klases.

    Funkcijas: iedot augsejo karti un samasit karsu kavu. Samainis eksistejoso kavu pret
    samaisto kavu.

    """

    def __init__(self):
        # Velak varetu uztaisit karsu klasi - (Card)
        self.deck = [Card(2, "Clubs"),
                     Card(3, "Clubs"),
                     Card(4, "Clubs"),
                     Card(5, "Clubs"),
                     Card(6, "Clubs"),
                     Card(7, "Clubs"),
                     Card(8, "Clubs"),
                     Card(9, "Clubs"),
                     Card(10, "Clubs"),
                     Card(10, "Clubs"),
                     Card(10, "Clubs"),
                     Card(10, "Clubs"),
                     Card(11, "Clubs"),
                     # spades
                     Card(2, "Spades"),
                     Card(3, "Spades"),
                     Card(4, "Spades"),
                     Card(5, "Spades"),
                     Card(6, "Spades"),
                     Card(7, "Spades"),
                     Card(8, "Spades"),
                     Card(9, "Spades"),
                     Card(10, "Spades"),
                     Card(10, "Spades"),
                     Card(10, "Spades"),
                     Card(10, "Spades"),
                     Card(11, "Spades"),
                     # hearts
                     Card(2, "Hearts"),
                     Card(3, "Hearts"),
                     Card(4, "Hearts"),
                     Card(5, "Hearts"),
                     Card(6, "Hearts"),
                     Card(7, "Hearts"),
                     Card(8, "Hearts"),
                     Card(9, "Hearts"),
                     Card(10, "Hearts"),
                     Card(10, "Hearts"),
                     Card(10, "Hearts"),
                     Card(10, "Hearts"),
                     Card(11, "Hearts"),
                     # diamonds
                     Card(2, "Diamonds"),
                     Card(3, "Diamonds"),
                     Card(4, "Diamonds"),
                     Card(5, "Diamonds"),
                     Card(6, "Diamonds"),
                     Card(7, "Diamonds"),
                     Card(8, "Diamonds"),
                     Card(9, "Diamonds"),
                     Card(10, "Diamonds"),
                     Card(10, "Diamonds"),
                     Card(10, "Diamonds"),
                     Card(10, "Diamonds"),
                     Card(11, "Diamonds")]
        self.shufleDeck()

    def giveCard(self):
        return self.deck.pop()

    def shufleDeck(self):
        copyDeck = self.deck.copy()
        shuffledDeck = []
        for i in range(len(copyDeck)):
            randomNumber = rand.randrange(len(copyDeck))
            shuffledDeck.append(copyDeck.pop(randomNumber))
        self.deck = shuffledDeck

# Bus divas apaksklases: House, Human


class Player():
    """
    Klase speletajs, izveido speletaju ar vardu un roku, kur glabat iedotas kartis ka ari
    naudu ar ko spelet.

    Funkcijas: aprekinat roku un izprintet roku.

    Speletajam uzreiz tiek aprekinata rokas summa.
    """

    def __init__(self, name, funds=100):
        self.name = name
        self.hand = []
        self.funds = funds

    # Funkcijas varetu but aprekinat karsu summu
    def calculateHandSum(self):
        sum = 0
        for i in self.hand:
            sum += i.value
        return sum
    # Uztaisism tuksu str funkciju

    def __str__(self) -> str:
        string = "{} hand | {} \n".format(self.name, self.calculateHandSum())
        for x in self.hand:
            string += str(x)
        return string

    def move(self):
        playerInput = input("Hit - h | Stand - l\n")
        if playerInput.lower() == "l":
            return 0
        elif playerInput.lower() == "h":
            return 1


# Mes sito dzeku kontrolesim


class Human(Player):
    """
    Klase cilveks ir apaksklase speletajam.

    Pievienotas ipasibas ir speles likme, kas pec noklusejuma ir 0.

    Pievienotas funkcijas ir likmes uzstadisana un izmaksa.
    """

    def __init__(self, name, funds=100, bet=0):
        super().__init__(name, funds)
        self.bet = bet

    def placeBet(self):
        self.funds -= self.bet

    def payout(self, payout):
        self.funds += payout

    def move():
        super().move()

    # sito velak bus jaizmaina! Paslaik vajag, lai saprotu ka suds strada

    def __str__(self) -> str:
        return super().__str__()


class Dealer(Player):
    """
    Klase dileris ir apaksklase speletajam

    """

    def __init__(self, name, hand):
        super().__init__(name, hand)

    # sito velak bus jaizmaina! Paslaik vajag, lai saprotu ka suds strada

    def __str__(self) -> str:
        return super().__str__()

    def first_hand_print(self):
        string = "{} hand | {} \n".format(
            self.name, self.calculateHandSum() - self.hand[1].value)
        for x in range(len(self.hand)-1):
            string += str(self.hand[x])
            if x < 1:
                string += " ---- "
                string += "\n|{}   |".format("X")
                string += "\n|    |"
                string += "\n|    |"
                string += "\n ---- \n"
        return string


# table = Table("Maris", "Dileris")
# print(table)

# player1 = Human("Maris")
# player1.move()

player2 = Player("Karlis")
player2.move()
