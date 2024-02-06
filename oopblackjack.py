import random as rand
# Ta pati deja cits stils

#TODO
"""
3. Edge case kad abas kartis var but Ace un pirmaja roka ja kada no kartim ir ace
3.1 Dilerim japiliek ka vins nem ace
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
        self.doubleAceSplit = False

        # Seit noteik speles seciba
        self.deal_first_hand()
        self.main()
        self.checkForWinner()
    # izdalam kartis

    def deal_first_hand(self):
        #for split tests
        self.player.hand.append(Card(11,"Spades", "ace"))
        self.dealer.hand.append(self.deck.giveCard())
        self.player.hand.append(Card(11,"Spades", "ace"))
        self.dealer.hand.append(self.deck.giveCard())

        # self.player.hand.append(self.deck.giveCard())
        # self.dealer.hand.append(self.deck.giveCard())
        # self.player.hand.append(self.deck.giveCard())
        # self.dealer.hand.append(self.deck.giveCard())

    # izprintejam informaciju par speletajiem
    def __str__(self):
        if (self.split == False):
            if (self.dealerMove or self.dealer.calculateHandSum(self.dealer.hand) == 21):
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
            if (self.dealerMove or self.dealer.calculateHandSum(self.dealer.hand) == 21):
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
    # main function
    def main(self):
        playerInput = ""
        # No sakuma speletajs kustas
        #uzliek naudu
        self.player.placeBet()
        self.doubleAceSplit = self.player.checkFirstHand()
        # Ja speletajam ir zem 21 tas spele
        while ((self.dealerMove == False and self.player.calculateHandSum(self.player.hand) < 21) or self.doubleAceSplit == True):
            # Paskatamies vai vispar vajag nemt kartis
            if (self.player.calculateHandSum(self.player.hand) >= 21 and self.doubleAceSplit != True):
                self.dealerMove = True
            # !!!VAJAG PARBAUDIT KADI IR SPELETAJA IESPEJAMIE GAJIENI
            # Ta lai tas nevar ievadit splitu, kad tas nemaz nevar splitot
            print(self)
            print(len(self.player.hand))
            
            if(self.doubleAceSplit == False):
                playerInput = self.player.move(self.moves, self.split)
            # Player stands
            if (playerInput == 0):
                self.dealerMove = True
            # Player hits
            elif (playerInput == 1):
                card = self.deck.giveCard()
                self.player.checkAce(card)
                self.player.hand.append(card)
                self.moves += 1
            # Player split
            elif ((playerInput == 2 and self.player.hand[0].name == self.player.hand[1].name and self.moves == 0) or self.doubleAceSplit == True):
                self.split = True
                # parbaudam vai pieteik nauda lai vispar veiktu split
                if (self.player.funds - self.player.bet >= 0):
                    # iedodam split deckam karti
                    self.player.splitHand.append(self.player.hand[1])
                    # Nonemam no orginala decka karti
                    self.player.hand.pop()
                    # need to check if we need to go to the second hand
                    moveHand = False
                    print(self.dealerMove)
                    while(self.dealerMove == False and moveHand == False):
                        if(self.player.calculateHandSum(self.player.hand) >= 21):
                            moveHand = True
                            break
                        print(self)
                        print("HAND 1 \|/")
                        playerInput = self.player.move(self.moves,self.split)
                        # There are two hands so if stand on the 1st go to the next hand
                        if (playerInput == 1 and moveHand!=True):
                            card = self.deck.giveCard()
                            self.player.checkAce(card)
                            self.player.hand.append(card)
                            self.moves += 1
                        elif (playerInput == 3 and self.moves == 0 and moveHand!=True):
                            if (self.player.funds - self.player.bet >= 0):
                                card = self.deck.giveCard()
                                self.player.checkAce(card)
                                self.player.hand.append(card)
                                self.moves += 1
                                moveHand = True
                                break
                            else:
                                print("You don't have enough money")
                                print("Your balance - {}$".format(self.player.funds))
                        elif(playerInput == 0):
                            moveHand = True
                            self.moves = 0
                            break
                        else:
                            print("Input a valid move!")
                    while(self.dealerMove == False):
                        if (self.player.calculateHandSum(self.player.splitHand) >= 21):
                            self.doubleAceSplit = False
                            self.dealerMove = True
                            break
                        print(self)
                        print("HAND 2 \|/")
                        playerInput = self.player.move(self.moves,self.split)
                        if (playerInput == 0):
                            self.dealerMove = True
                            self.doubleAceSplit = False
                            break
                        elif (playerInput == 1):
                            card = self.deck.giveCard()
                            self.player.checkAce(card)
                            self.player.splitHand.append(card)
                            self.moves += 1
                        elif (playerInput == 3 and self.moves == 0):
                            if (self.player.funds - self.player.bet >= 0):
                                card = self.deck.giveCard()
                                self.player.checkAce(card)
                                self.player.splitHand.append(card)
                                self.moves += 1
                                self.dealerMove = True
                                self.doubleAceSplit = False
                                break
                            else:
                                print("You don't have enough money")
                                print("Your balance - {}$".format(self.player.funds))
                        else:
                            print("Input a valid move!")
                        
                else:
                    print("You don't have enough money")
                    print("Your balance - {}$".format(self.player.funds))

            # Double down
            elif (playerInput == 3 and self.moves == 0):
                if (self.player.funds - self.player.bet >= 0):
                    card = self.deck.giveCard()
                    self.player.checkAce(card)
                    self.player.hand.append(card)
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
        while (self.dealerMove and self.dealer.calculateHandSum(self.dealer.hand) != 21):
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
    # Resests the deck if cards are below 10
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

    def __init__(self, value, suit, name):
        self.value = value
        self.suit = suit
        self.name = name


class Deck():

    """
    Karsu kavas klase, kurai ipasibas bus kava un kavu samaisisanam, kur kavu uzreiz samaisis.
    Kavai kartis tiek veidotas no karsu klases.

    Funkcijas: iedot augsejo karti un samasit karsu kavu. Samainis eksistejoso kavu pret
    samaisto kavu.

    """

    def __init__(self):
        # I should add a symbol for kings, queens, aces and jacks
        self.deck = []
        for value in range(2, 17):
            for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]:
                if value == 2:
                    self.deck.append(Card(value, suit, "two"))
                elif value == 3:
                    self.deck.append(Card(value, suit, "three"))
                elif value == 4:
                    self.deck.append(Card(value, suit, "four"))
                elif value == 5:
                    self.deck.append(Card(value, suit, "five"))
                elif value == 6:
                    self.deck.append(Card(value, suit, "six"))
                elif value == 7:
                    self.deck.append(Card(value, suit, "seven"))
                elif value == 8:
                    self.deck.append(Card(value, suit, "eight"))
                elif value == 9:
                    self.deck.append(Card(value, suit, "nine"))
                elif value == 10:
                    self.deck.append(Card(value, suit, "ten"))
                elif value == 11:
                    self.deck.append(Card(10, suit, "jack"))
                elif value == 12:
                    self.deck.append(Card(10, suit, "queen"))
                elif value == 13:
                    self.deck.append(Card(10, suit, "king"))
                elif value == 14:
                    self.deck.append(Card(11, suit, "ace"))
                else:
                    pass
        self.shufleDeck()

    def giveCard(self):
        card = self.deck.pop()
        return card

    def shufleDeck(self):
        copyDeck = self.deck.copy()
        shuffledDeck = []
        for i in range(len(copyDeck)):
            randomNumber = rand.randrange(len(copyDeck))
            shuffledDeck.append(copyDeck.pop(randomNumber))
        self.deck = shuffledDeck
        
    

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

    # This function does not have self thus it is static.
    # Didnt give it self because there is a split condition.
    # Don't want to create a new function just for split hand.
    @staticmethod
    def calculateHandSum(hand):
        sum = 0
        for i in hand:
            sum += i.value
        return sum
    
    @staticmethod
    def printLineDown(hand):
        string = ""
        for _ in range(len(hand)):
            string += " ----- "
        return string
    
    @staticmethod
    def printStraightLine(hand):
        string = ""
        for _ in range(len(hand)):
            string += "|     |"
        return string
    
    def printSymbol(self, i):
        string = ""
        if (i.value > 9):
            if (i.name == "jack"):
                string += str(("|{}/{}  |".format("J", i.suit_unicode[i.suit])))
            elif (i.name == "queen"):
                string += str(("|{}/{}  |".format("Q", i.suit_unicode[i.suit])))
            elif (i.name == "king"):
                string += str(("|{}/{}  |".format("K", i.suit_unicode[i.suit])))  
            elif (i.name == "ace"):
                string += str(("|{}/{}  |".format("A", i.suit_unicode[i.suit])))
            else:
                string += str(("|{}/{} |".format(i.value, i.suit_unicode[i.suit])))
        else:
            if (i.name == "ace"):
                string += str(("|{}/{}  |".format("A", i.suit_unicode[i.suit])))
            else:
                string += str(("|{}/{}  |".format(i.value, i.suit_unicode[i.suit])))
        return string

    def __str__(self) -> str:
        string = ("{} Hand Sum - {} | Bet - {}\n".format(
            self.name, self.calculateHandSum(self.hand), self.bet)) 
        string += self.printLineDown(self.hand) + "\n"
        for i in self.hand:
            string  += self.printSymbol(i)
        string += "\n" + self.printStraightLine(self.hand)
        string += "\n" + self.printStraightLine(self.hand) + "\n"
        string += self.printLineDown(self.hand)
        return string


# Mes sito dzeku kontrolesim


class Human(Player):
    """
    Klase cilveks ir apaksklase speletajam.

    Pievienotas ipasibas ir speles likme, kas pec noklusejuma ir 0.

    Pievienotas funkcijas ir likmes uzstadisana un izmaksa.
    """
    #same as dealer only has bet and split hand
    def __init__(self, name, bet=0):
        super().__init__(name)
        self.bet = bet
        self.splitHand = []
    #places a bet
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
    #gives player money
    def payout(self, payout):
        self.funds += payout
    #checks if player has split
    def checkForSplit(self):
        if (self.hand[0].name == self.hand[1].name):
            return True
        else:
            return False
    #all the possible moves for player, moves are checked in the main function
    def move(self, moves, split):
        if(split == True):
            if (moves == 0):
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
        else:
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

    #prints cards if input is split
    def split_print(self):
        string = "Hand 1 SUM - {} \t\n".format(
            self.calculateHandSum(self.hand))
        string += self.printLineDown(self.hand) + "\n"
        for i in self.hand:
            string  += self.printSymbol(i)
        string += "\n" + self.printStraightLine(self.hand)
        string += "\n" + self.printStraightLine(self.hand) + "\n"
        string += self.printLineDown(self.hand) + "\n"
        string += "Hand 2 SUM - {} \t\n".format(
                    self.calculateHandSum(self.splitHand))
        string += self.printLineDown(self.splitHand) + "\n"
        for i in self.splitHand:
            string  += self.printSymbol(i)
        string += "\n" + self.printStraightLine(self.splitHand)
        string += "\n" + self.printStraightLine(self.splitHand) + "\n"
        string += self.printLineDown(self.splitHand) + "\n"
        return string
    #prints cards
    def __str__(self) -> str:
        return super().__str__()

    def checkAce(self,card):
        if(card.name == "ace" and self.calculateHandSum(self.hand) + card.value > 21):
            card.value = 1
        elif(card.name == "ace"):
            while(True):
                playerinput = input("Choose ace value!(1/11)")
                if (playerinput == "1"):
                    card.value = 1
                    break
                elif (playerinput == "11"):
                    card.value = 11
                    break
                else:
                    print("input 1 or 11")
    
    def checkFirstHand(self):
        if(self.hand[0].name == "ace" and self.hand[1].name == "ace"):
            while(True):
                print("YIKES you got two aces!")
                playerInput = input("Choose hand value! (2/12) or s-split")
                if(playerInput == "2"):
                    self.hand[0].value = 1
                    self.hand[1].value = 1
                    return False
                elif(playerInput == "12"):
                    self.hand[1].value = 1
                    return False
                elif(playerInput == "s"):
                    return True
                else:
                    print("input 2, 12 or s")
        elif(self.hand[0].name == "ace" or self.hand[1].name == "ace"):
            for card in self.hand:
                if(card.name == "ace"):
                    while(True):
                        print("You got a ace!")
                        playerInput = input("Choose a ace value! (1/11) ")
                        if(playerInput == "1"):
                            card.value = 1
                            return False
                        elif(playerInput == "11"):
                            card.value = 11
                            return False
                        else:
                            print("input 1 or 11")
                    
                        
class Dealer(Player):
    """
    Klase dileris ir apaksklase speletajam
    """
    #Has the same properties as player class 
    def __init__(self, name):
        super().__init__(name)

    #pirnts cards
    def __str__(self) -> str:
        string = ("{} Hand Sum - {} |\n".format(
        self.name, self.calculateHandSum(self.hand))) 
        string += self.printLineDown(self.hand) + "\n"
        for i in self.hand:
            string  += self.printSymbol(i)
        string += "\n" + self.printStraightLine(self.hand)
        string += "\n" + self.printStraightLine(self.hand) + "\n"
        string += self.printLineDown(self.hand)
        return string
    #prints cards but hides the second one
    def first_hand_print(self):
        string = "{} hand | {} \n".format(
            self.name, self.calculateHandSum(self.hand) - self.hand[1].value)
        string += self.printLineDown(self.hand) + "\n"
        for i in self.hand:
            string  += self.printSymbol(i)
            string += str(("|{}/{}  |".format("x", "?")))
            string += "\n" + self.printStraightLine(self.hand)
            string += "\n" + self.printStraightLine(self.hand) + "\n"
            string += self.printLineDown(self.hand)
            break
        return string
    #makes move based on player hand
    def move(self, playerHand):
        if (self.calculateHandSum(self.hand) < 17 and playerHand.calculateHandSum(playerHand.hand) > self.calculateHandSum(self.hand)):
            return True
        return False


table = Table("Maris", "Dileris")
