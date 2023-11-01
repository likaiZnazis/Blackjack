import random as rand
# Ta pati deja cits stils


class Table():

    """
    Table klase bus vieta kur visas klases saies kopa.
    Stradas ari kopa, piemeram, kavas klase stradas
    kopa ar dileri un playeri. Ka ari protmas galvena
    cilpa kur notiks visa speles seciba. Parbuadit
    kurs ir uzvaretajs
    """
    # inicializejam galdu kur parametri ir speletaja un dilera vardi
    # Ipasibas ir Speletajs, Dileris un Kava kur ir ieksa kartis

    def __init__(self, player, dealer):
        self.player = Human(player)
        self.dealer = Dealer(dealer)
        self.deck = Deck()
        self.dealerMove = False
        self.moves = 0
        self.input = 0

        # Seit noteik speles seciba
        self.deal_first_hand()
        self.main()
        self.checkForWinner()
    # izdalam kartis

    def deal_first_hand(self):
        self.player.hand.append(self.deck.giveCard())
        self.dealer.hand.append(self.deck.giveCard())
        self.player.hand.append(self.deck.giveCard())
        self.dealer.hand.append(self.deck.giveCard())
    # izprintejam informaciju par speletajiem

    def __str__(self):
        if (self.dealerMove or self.dealer.calculateHandSum() == 21):
            string = "{}".format(self.dealer)
            string += "\n\n\n\n\n\n"
            string += "{}".format(self.player)
            return string
        else:
            string = "{}".format(self.dealer.first_hand_print())
            string += "\n\n\n\n\n\n"
            string += "{}".format(self.player)
            return string
    # galvena cilpa jeb speles solu seciba

    def main(self):

        # No sakuma speletajs kustas
        self.player.placeBet()
        # Paskatamies vai vispar vajag nemt kartis
        if (self.player.calculateHandSum() == 21):
            self.dealerMove = True
        # Ja speletajam ir zem 21 tas spele
        while (self.dealerMove == False and self.player.calculateHandSum() < 21):
            # !!!VAJAG PARBAUDIT KADI IR SPELETAJA IESPEJAMIE GAJIENI
            # Ta lai tas nevar ievadit splitu, kad tas nemaz nevar splitot
            print(self)
            playerInput = self.player.move(self.moves)
            # Player stands
            if (playerInput == 0):
                self.dealerMove = True
            # Player hits
            elif (playerInput == 1):
                self.player.hand.append(self.deck.giveCard())
                self.moves += 1
            # Player split
            elif (playerInput == 2):
                pass
            # Double down
            elif (playerInput == 3):
                pass
        # Seit dileris kustas
        """
        Seit mes skatamies vai nav vienads ar 21, lai parliecinatos, ka
        nav blackjack. Tadejadi mums nevajadzes lieki veikt 1 iteraciju
        """
        while (self.dealerMove and self.dealer.calculateHandSum() != 21):
            # Ja ir janem karti
            if (self.dealer.move() == True):
                # Tas nems karti
                self.dealer.hand.append(self.deck.giveCard())
                print(self)
            else:
                # Preteji tas beigs gajienu
                self.dealerMove = False
    # parbaudam kurs uzvareja speli

    # JAPAPILDINA AR VEL UZVARAS KONDICIJAM
    def checkForWinner(self):
        # Man neintrese vai dilerim ir blackjacks
        # Man tikai intrese dilera karsu summa
        # Seit mes skatamies vai speletajam ir blackjacks
        # un dilerim 21
        print(self)
        if (self.moves == 0 and self.player == 21 and self.dealer == 21):
            print("No one wins!")
        elif (self.moves == 0 and self.player == 21):
            print("Player got BLACKJACK! - {}")


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

        self.deck = [Card(value, suit) for value in range(2, 12)
                     for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]]
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

    def __str__(self) -> str:
        string = ""
        for x in self.deck:
            string += str(x)
        return string

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

# Mes sito dzeku kontrolesim


class Human(Player):
    """
    Klase cilveks ir apaksklase speletajam.

    Pievienotas ipasibas ir speles likme, kas pec noklusejuma ir 0.

    Pievienotas funkcijas ir likmes uzstadisana un izmaksa.
    """

    def __init__(self, name, bet=0):
        super().__init__(name)
        self.bet = bet

    def placeBet(self):
        while (True):
            print("You have {}$".format(str(self.funds)))
            try:
                playerInput = int(input("Place your bet\n"))
            except:
                print("Input just a number!")
            else:
                self.bet = playerInput
                self.funds -= self.bet
                break

    def payout(self, payout):
        self.funds += payout

    def checkForSplit(self):
        if (self.hand[0].value == self.hand[1].value):
            return True
        else:
            return False
# Si funkcija illustres iespejamos gajienus speletajm
# Vajag vel ielikt loopu ja nepareiz inputs tiek ievadits

    def move(self, moves):
        if (self.checkForSplit() and moves == 0):
            playerInput = input(
                "Hit - h | Stand - l| Split - s| Double down - d\n")
            if playerInput.lower() == "l":
                return 0
            elif playerInput.lower() == "h":
                return 1
            elif playerInput.lower() == "s":
                return 2
            elif playerInput.lower() == "d":
                return 3
        elif (moves == 0):
            playerInput = input(
                "Hit - h | Stand - l| Double down - d\n")
            if playerInput.lower() == "l":
                return 0
            elif playerInput.lower() == "h":
                return 1
            elif playerInput.lower() == "d":
                return 3
        else:
            playerInput = input("Hit - h | Stand - l\n")
            if playerInput.lower() == "l":
                return 0
            elif playerInput.lower() == "h":
                return 1

    # sito velak bus jaizmaina! Paslaik vajag, lai saprotu ka suds strada

    def __str__(self) -> str:
        string = "{} Hand Sum - {} | Bet - {}\n".format(
            self.name, self.calculateHandSum(), self.bet)
        for x in self.hand:
            string += str(x)
        return string


class Dealer(Player):
    """
    Klase dileris ir apaksklase speletajam

    """

    def __init__(self, name):
        super().__init__(name)

    # sito velak bus jaizmaina! Paslaik vajag, lai saprotu ka suds strada

    def __str__(self) -> str:
        string = "{} Hand - {} Sum - {}\n".format(
            self.name, self.calculateHandSum())
        for x in self.hand:
            string += str(x)
        return string

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

    def move(self):
        if (self.calculateHandSum() < 17 and Human.calculateHandSum() > self.calculateHandSum()):
            return True
        return False


table = Table("Maris", "Dileris")
