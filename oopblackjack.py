import random as rand
# Ta pati deja cits stils

#TODO
"""
1. Kartim vajag: Karali, Damu, Piki, Duzi. Japieliek velviena ipasiba = name
2. Sacinit splitu
3. Edge case, kad pirmas kartis abas ir ace
4. Winning conditions


"""

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
        self.split = False

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
        if (self.split == False):
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
        else:
            if (self.dealerMove or self.dealer.calculateHandSum() == 21):
                # if dealer has 21 it prints its whole hand
                string = "{}".format(self.dealer)
                string += "\n\n\n\n\n\n"
                string += "{}".format(self.player.split_print())
                return string
            else:
                string = "{}".format(self.dealer.first_hand_print())
                string += "\n\n\n\n\n\n"
                string += "{}".format(self.player.split_print())
                return string
    # galvena cilpa jeb speles solu seciba

    def main(self):

        # No sakuma speletajs kustas
        #uzliek naudu
        self.player.placeBet()

        # Ja speletajam ir zem 21 tas spele
        while (self.dealerMove == False and self.player.calculateHandSum() < 21):
            # Paskatamies vai vispar vajag nemt kartis
            if (self.player.calculateHandSum() >= 21):
                self.dealerMove = True
            print(self.moves)
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
            elif (playerInput == 2 and self.player.hand[0].value == self.player.hand[0].value and self.moves == 0):
                # parbaudam vai pieteik nauda lai vispar veiktu split
                if (self.player.funds - self.player.bet >= 0):
                    self.split = True
                    # iedodam split deckam karti
                    self.player.splitDeck.append(self.player.hand[1])
                    # Nonemam no orginala decka karti
                    self.player.hand.pop()
                    # izprintejam decku
                    print(self)
                else:
                    print("You don't have enough money")
                    print("Your balance - {}$".format(self.player.funds))

                pass

            # Double down
            elif (playerInput == 3 and self.moves == 0):
                if (self.player.funds - self.player.bet >= 0):
                    self.player.hand.append(self.deck.giveCard())
                    self.moves += 1
                    self.dealerMove = True
                else:
                    print("You don't have enough money")
                    print("Your balance - {}$".format(self.player.funds))
            else:
                print("Input a valid move!")
        # Seit dileris kustas
        """
        Seit mes skatamies vai nav vienads ar 21, lai parliecinatos, ka
        nav blackjack. Tadejadi mums nevajadzes lieki veikt 1 iteraciju
        """
        while (self.dealerMove and self.dealer.calculateHandSum() != 21):
            # Ja ir janem karti
            if (self.dealer.move(self.player) == True):
                # Tas nems karti
                self.dealer.hand.append(self.deck.giveCard())
                print(self)
            else:
                # Preteji tas beigs gajienu
                break

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

    def resetAll(self):
        pass


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


class Deck():

    """
    Karsu kavas klase, kurai ipasibas bus kava un kavu samaisisanam, kur kavu uzreiz samaisis.
    Kavai kartis tiek veidotas no karsu klases.

    Funkcijas: iedot augsejo karti un samasit karsu kavu. Samainis eksistejoso kavu pret
    samaisto kavu.

    """

    def __init__(self):
        # I should add a symbol for kings, queens, aces and jacks
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
            string += str
        return ""
        

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
    
    def printLineDown(self):
        string = ""
        for i in range(len(self.hand)):
            string += " ----- "
        return string

    def printStraightLine(self):
        string = ""
        for i in range(len(self.hand)):
            string += "|     |"
        return string
    
    def __str__(self) -> str:
        
        string = ("{} Hand Sum - {} | Bet - {}\n".format(
            self.name, self.calculateHandSum(), self.bet)) 
        string += self.printLineDown() + "\n"
        for i in self.hand:
            if (i.value > 9):
                string += str(("|{}/{} |".format(i.value, i.suit_unicode[i.suit])))
            else:
                string += str(("|{}/{}  |".format(i.value, i.suit_unicode[i.suit])))
        string += "\n" + self.printStraightLine()
        string += "\n" + self.printStraightLine() + "\n"
        string += self.printLineDown()
        return string

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
        self.splitDeck = []

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
    def calculateSplitDeck(self):
        sum = 0
        for x in self.splitDeck:
            sum += x
        return sum

    def split_print(self):
        string = "Hand 1 SUM - {} \t\tHand 2 SUM - {}\n".format(
            self.calculateHandSum(), self.calculateSplitDeck())
        string += ""

    def __str__(self) -> str:
        return super().__str__()

class Dealer(Player):
    """
    Klase dileris ir apaksklase speletajam

    """

    def __init__(self, name):
        super().__init__(name)

    # sito velak bus jaizmaina! Paslaik vajag, lai saprotu ka suds strada

    def __str__(self) -> str:
        return super().__str__()

    def first_hand_print(self):
        string = "{} hand | {} \n".format(
            self.name, self.calculateHandSum() - self.hand[1].value)
        string += self.printLineDown() + "\n"
        for i in self.hand:
            if (i.value > 9):
                string += str(("|{}/{} |".format(i.value, i.suit_unicode[i.suit])))
            else:
                string += str(("|{}/{}  |".format(i.value, i.suit_unicode[i.suit])))
            string += str(("|{}/{}  |".format("x", "?")))
            string += "\n" + self.printStraightLine()
            string += "\n" + self.printStraightLine() + "\n"
            string += self.printLineDown()
            break
        return string

    def move(self, playerHand):
        if (self.calculateHandSum() < 17 and playerHand.calculateHandSum() > self.calculateHandSum()):
            return True
        return False


table = Table("Maris", "Dileris")
