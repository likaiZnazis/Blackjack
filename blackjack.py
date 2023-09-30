import random as rand

# Deck consists of 52 cards excluding jokers. 4 suits x 13 different types of cards


# clubs

twoC = {"value": 2, "name": "two", "suit": "Clubs"}
threeC = {"value": 3, "name": "three", "suit": "Clubs"}
fourC = {"value": 4, "name": "four", "suit": "Clubs"}
fiveC = {"value": 5, "name": "five", "suit": "Clubs"}

sixC = {"value": 6, "name": "six", "suit": "Clubs"}
sevenC = {"value": 7, "name": "seven", "suit": "Clubs"}
eightC = {"value": 8, "name": "eight", "suit": "Clubs"}
nineC = {"value": 9, "name": "nine", "suit": "Clubs"}
tenC = {"value": 10, "name": "ten", "suit": "Clubs"}
jackC = {"value": 10, "name": "jack", "suit": "Clubs"}
queenC = {"value": 10, "name": "queen", "suit": "Clubs"}
kingC = {"value": 10, "name": "king", "suit": "Clubs"}
aceC = {"value": 11, "name": "ace", "suit": "Clubs"}

# spades

twoS = {"value": 2, "name": "two", "suit": "Spades"}
threeS = {"value": 3, "name": "three", "suit": "Spades"}
fourS = {"value": 4, "name": "four", "suit": "Spades"}
fiveS = {"value": 5, "name": "five", "suit": "Spades"}
sixS = {"value": 6, "name": "six", "suit": "Spades"}
sevenS = {"value": 7, "name": "seven", "suit": "Spades"}
eightS = {"value": 8, "name": "eight", "suit": "Spades"}
nineS = {"value": 9, "name": "nine", "suit": "Spades"}
tenS = {"value": 10, "name": "ten", "suit": "Spades"}
jackS = {"value": 10, "name": "jack", "suit": "Spades"}
queenS = {"value": 10, "name": "queen", "suit": "Spades"}
kingS = {"value": 10, "name": "king", "suit": "Spades"}
aceS = {"value": 11, "name": "ace", "suit": "Spades"}

# hearts

twoH = {"value": 2, "name": "two", "suit": "Hearts"}
threeH = {"value": 3, "name": "three", "suit": "Hearts"}
fourH = {"value": 4, "name": "four", "suit": "Hearts"}
fiveH = {"value": 5, "name": "five", "suit": "Hearts"}
sixH = {"value": 6, "name": "six", "suit": "Hearts"}
sevenH = {"value": 7, "name": "seven", "suit": "Hearts"}
eightH = {"value": 8, "name": "eight", "suit": "Hearts"}
nineH = {"value": 9, "name": "nine", "suit": "Hearts"}
tenH = {"value": 10, "name": "ten", "suit": "Hearts"}

jackH = {"value": 10, "name": "jack", "suit": "Hearts"}
queenH = {"value": 10, "name": "queen", "suit": "Hearts"}
kingH = {"value": 10, "name": "king", "suit": "Hearts"}
aceH = {"value": 11, "name": "ace", "suit": "Hearts"}

# diamonds

twoD = {"value": 2, "name": "two", "suit": "Diamonds"}
threeD = {"value": 3, "name": "three", "suit": "Diamonds"}
fourD = {"value": 4, "name": "four", "suit": "Diamonds"}
fiveD = {"value": 5, "name": "five", "suit": "Diamonds"}
sixD = {"value": 6, "name": "six", "suit": "Diamonds"}
sevenD = {"value": 7, "name": "seven", "suit": "Diamonds"}
eightD = {"value": 8, "name": "eight", "suit": "Diamonds"}

nineD = {"value": 9, "name": "nine", "suit": "Diamonds"}
tenD = {"value": 10, "name": "ten", "suit": "Diamonds"}
jackD = {"value": 10, "name": "jack", "suit": "Diamonds"}
queenD = {"value": 10, "name": "queen", "suit": "Diamonds"}
kingD = {"value": 10, "name": "king", "suit": "Diamonds"}
aceD = {"value": 11, "name": "ace", "suit": "Diamonds"}


deckOfCards = [
    twoC,
    twoD,
    twoH,
    twoS,
    threeC,
    threeD,
    threeH,
    threeS,
    fourC,
    fourD,
    fourH,
    fourS,
    fiveC,
    fiveD,
    fiveH,
    fiveS,
    sixC,
    sixD,
    sixH,
    sixS,
    sevenC,
    sevenD,
    sevenH,
    sevenS,
    eightC,
    eightD,
    eightH,
    eightS,
    nineC,
    nineD,
    nineH,
    nineS,
    tenC,
    tenD,
    tenH,
    tenS,
    jackC,
    jackD,
    jackH,
    jackS,
    queenC,
    queenD,
    queenH,
    queenS,
    kingC,
    kingD,
    kingH,
    kingS,
    aceC,
    aceD,
    aceH,
    aceS,
]
""""
playing cards suits in unicode, has a problem that its in different sizes.

""" 
def printLineDown(deckSize):
	string = ""
	for i in range(len(deckSize)):
		string += " ---- "
	return string

def printStraightLine(deck):
	string = ""
	for i in range(len(deck)):
		string += "|    |"
	return string

def convertSuit(suit):
	if suit == "Diamonds":
		return u'\u2666'
	elif suit == "Hearts":
		return u'\u2665'
	elif suit == "Spades":
		return u'\u2660'
	else:
		return u'\u2663'

def shuffle():
    copyDeck = deckOfCards.copy()
    shuffledDeck = []
    for i in range(len(copyDeck)):
        randomNumber = rand.randrange(len(copyDeck))
        shuffledDeck.append(copyDeck.pop(randomNumber))
    return shuffledDeck
def dealCards():
    player.append(shuffledDeck.pop())
    house.append(shuffledDeck.pop())
    player.append(shuffledDeck.pop())
    #two aci time
    #player.append(aceD)
    #player.append(aceH)
    house.append(shuffledDeck.pop())
    printCards(False)
def aces(playerHand):
    if playerHand[0]["name"] == "ace" or playerHand[1]["name"] == "ace":
        return True
    return False
def checkPlayerCards(playerHand, money, bet):
    # edge case when both cards are aces, alot of options :/
    if playerHand[0]["name"] == "ace" and playerHand[1]["name"] == "ace":
        while True:
            playerChoice = input("Choose a value 2 or 12 or s - split\n -")
            if playerChoice == str(12):
                playerHand[0]["value"] = 1
                playerHand[1]["value"] = 11
                return False, [], [], False, False
            elif playerChoice == str(2):
                playerHand[0]["value"] = 1
                playerHand[1]["value"] = 1
                return False, [], [], False, False
            elif playerChoice == "s":
                if money - bet >= 0:
                    money -= bet
                    bet += bet
                    split = True
                    handOne = [playerHand[0]]
                    handTwo = [playerHand[1]]
                    print(bet)
                    dealerMove, printHandOne = spliting(handOne, handTwo, bet)
                    return split, handOne, handTwo, printHandOne, dealerMove, money, bet
                else:
                    print("YOU DONT HAVE ENOUGH MONEY :()")
            else:
                print("Not valid input")
    # Gives the option to choose between two ace values 1 or 11
    elif calculateScore(playerHand) < 21:
        for i in playerHand:
            if i["name"] == "ace":
                while True:
                    aceValue = input(
                        "Choose {}\{} \n -".format(
                            calculateScore(playerHand) - 10, calculateScore(playerHand)
                        )
                    )
                    if aceValue == str(calculateScore(playerHand) - 10):
                        i["value"] = 1
                        break
                    elif aceValue == str(calculateScore(playerHand)):
                        i["value"] = 11
                        break
                    else:
                        print("Not valid input!")
                        #split, handOne, handTwo, printHandOne, dealerMove = checkPlayerCards(player)
        return False, [], [], False, False, money, bet
def printHouseCardsUp():
    print("\tHOUSE HAND - {} \n".format(calculateScore(house)))
    string = ""
    string += (printLineDown(house) + "\n")
    #need to look at the value if the value is double digits then
    #i have to print it in a different way
    for i in house:
        #double
        if (i["value"] > 9):
            string += ("|{}{} |".format(i["value"], convertSuit(i["suit"])))
        else:
            string += ("|{}{}  |".format(i["value"], convertSuit(i["suit"])))
    string += ("\n" + printStraightLine(house))
    string += ("\n" + printStraightLine(house)+ "\n")
    string += ( printLineDown(house))
    print(string)
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
def printHouseCardsDown():
    print("\tHOUSE HAND - {} \n".format(calculateScore(house)))
    string = ""
    string += (printLineDown(house) + "\n")
    if (house[0]["value"] > 9):
        string += ("|{}{} || X  |".format(house[0]["value"], convertSuit(house[0]["suit"])))
    else:
        string += ("|{}{}  || X  |".format(house[0]["value"], convertSuit(house[0]["suit"])))
    string += ("\n" + printStraightLine(house))
    string += ("\n" + printStraightLine(house) + "\n")
    string += ( printLineDown(house))
    print(string)
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
def printPlayerCards():
    string = ""
    string += (printLineDown(player) + "\n")
    #need to look at the value if the value is double digits then
    #i have to print it in a different way
    for i in player:
        #double
        if (i["value"] > 9):
            string += ("|{}{} |".format(i["value"], convertSuit(i["suit"])))
        else:
            string += ("|{}{}  |".format(i["value"], convertSuit(i["suit"])))
    string += ("\n" + printStraightLine(player))
    string += ("\n" + printStraightLine(player)+ "\n")
    string += ( printLineDown(player))
    print(string)
    print("\n")
    print("\tPLAYER HAND| {}\t \n ".format(calculateScore(player)))
    print("BET - {}".format(bet))
def calculateScore(array):
    sumPlayer = 0
    for i in array:
        sumPlayer = sumPlayer + int(i["value"])
    return sumPlayer
# not working perfectly in the second hand
def splitPrint(handOne, handTwo, printHandOne, bet):
    print(bet)
    control = 0
    string = ""
    if printHandOne == True:
        for j in handTwo:
            for i in handOne:
                if control == 0:
                    string += "\t\t{:2},{:8} \t {:2},{:8} \n".format(
                        i["value"], i["suit"], j["value"], j["suit"]
                    )
                    control += 1
                else:
                    string += "\t\t{:2},{:8}\n".format(i["value"], i["suit"])
        print(string)
        print(
            "PLAYER\t\tHAND 1| {}\t\tHAND 2| {}".format(
                calculateScore(handOne), calculateScore(handTwo)
            )
        )
        print("BET - {}".format(bet))
    else:
        for j in range(len(handTwo)):
            if j < len(handOne):
                string += "\t\t{:2},{:8} \t {:2},{:8} \n".format(
                    handOne[j]["value"],
                    handOne[j]["suit"],
                    handTwo[j]["value"],
                    handTwo[j]["suit"],
                )
            else:
                string += "\t\t\t\t {:2},{:8} \n".format(
                    handTwo[j]["value"], handTwo[j]["suit"]
                )
        print(string)

        print(
            "PLAYER\t\tHAND 1| {}\t\tHAND 2| {}".format(
                calculateScore(handOne), calculateScore(handTwo)
            )
        )
        print("BET - {}".format(bet))
# prob can shorten the code here
def printWinner():
    returnMoney = bet
    if split != True:
        if calculateScore(player) > 21:
            returnMoney = 0
            print("BUST")
        elif calculateScore(player) == calculateScore(house):
            print("TIE")
        elif calculateScore(player) == 21 and move == 0:
            returnMoney = returnMoney * 1.5
            print("BLACKJACK")
        elif calculateScore(house) > 21:
            returnMoney += returnMoney
            print("HOUSE BUSTS")
        elif calculateScore(player) > calculateScore(house):
            returnMoney += returnMoney
            print("PLAYER WINS WITH {} POINTS".format(calculateScore(player)))
        elif calculateScore(player) < calculateScore(house):
            returnMoney = 0
            print("HOUSE WINS WITH {} POINTS".format(calculateScore(house)))
    else:
        if(calculateScore(handOne) <= 21 and calculateScore(handTwo) <= 21 and calculateScore(house) <= 21):
            if(calculateScore(handOne) == calculateScore(house) and calculateScore(handTwo) == calculateScore(house)):
                returnMoney = returnMoney
                print("YOU MATCHED ON BOTH HANDS")
            elif(calculateScore(handOne) > calculateScore(house) and calculateScore(handTwo) > calculateScore(house)):
                returnMoney += returnMoney
                print("YOU WON ON BOTH HANDS")
            elif(calculateScore(handOne) > calculateScore(house)):
                returnMoney = returnMoney / 2
                print("YOU WON THE FIRST HAND")
            elif(calculateScore(handTwo) > calculateScore(house)):
                returnMoney = returnMoney / 2
                print("YOU WON THE SECOND HAND")
            else:
                returnMoney = 0
                print("YOU LOST BOTH HANDS")
        elif(calculateScore(house) > 21):
            if(calculateScore(handOne) <= 21 and calculateScore(handTwo) <= 21):
                returnMoney += returnMoney
                print("YOU WON BOTH HANDS")
            elif(calculateScore(handOne) <= 21):
                returnMoney = returnMoney / 2
                print("YOU WON THE FIRST HAND")
            elif(calculateScore(handTwo) <= 21):
                returnMoney = returnMoney / 2
                print("YOU WON THE SECOND HAND")
            else:
                returnMoney = 0
                print("YOU LOST BOTH HANDS")
        elif(calculateScore(handOne) > 21 or calculateScore(handTwo) > 21):
            if(calculateScore(handOne) <= 21
               and calculateScore(house) < calculateScore(handOne)):
                returnMoney = returnMoney / 2
                print("YOU WON THE FIRST HAND")
            elif(calculateScore(handTwo) <= 21
                 and calculateScore(house) < calculateScore(handTwo)):
                returnMoney = returnMoney / 2
                print("YOU WON THE SECOND HAND")
            elif(calculateScore(handOne) == calculateScore(house)):
                returnMoney = returnMoney / 2
                print("YOU MATCHED THE FIRST HAND")
            elif(calculateScore(handTwo) == calculateScore(house)):
                returnMoney = returnMoney / 2
                print("YOU MATCHED THE SECOND HAND")
            
            else:
                returnMoney = 0
                print("YOU LOST BOTH HANDS")
        else:
            if(calculateScore(handOne) == calculateScore(house)):
                returnMoney = returnMoney / 2
                print("YOU MATHCED THE FIRST HAND")
            elif(calculateScore(handTwo) == calculateScore(house)):
                returnMoney = returnMoney / 2
                print("YOU MATCHED THE SECOND HAND")
            else:
                returnMoney = 0
                print("YOU LOST BOTH HANDS")
    return returnMoney
    
def drawCard(hand, dealersMove):
    topCard = shuffledDeck.pop()
    if dealersMove:
        if topCard["name"] == "ace" and calculateScore(hand) + 11 > 21:
            topCard["value"] = 1
        #if i make just an else statement not elif it will change random card values to 11 :-|
        elif topCard["name"] == "ace" and calculateScore(hand) + 11 < 21:
            topCard["value"] = 11
    else:
        if topCard["name"] == "ace" and calculateScore(hand) + 11 > 21:
            topCard["value"] = 1
        elif topCard["name"] == "ace" and calculateScore(hand) + 11 < 21:
            while True:
                print("Choose ace value 1 or 11")
                playerInput = input("-")
                if playerInput == str(1):
                    topCard["value"] = 1
                    break
                elif playerInput == str(11):
                    topCard["value"] = 11
                    break
                else:
                    print("Not valid input!")
    hand.append(topCard)
def dealersMove(*args):
    # dealersMove(split, handOne, handTwo, printHandOne)
    if args[0] != True:
        printCards(args[0])
        while calculateScore(house) < 17 and calculateScore(house) < calculateScore(player) and calculateScore(player) <= 21:
            drawCard(house,True)
            printCards(args[0])
    else:
        printCards(args[0], args[1], args[2], args[3], args[4])
        while (
            calculateScore(args[1]) > calculateScore(house)
            and calculateScore(house) < 17
            and calculateScore(args[1]) <= 21
        or 
            calculateScore(args[2]) > calculateScore(house)
            and calculateScore(house) < 17
            and calculateScore(args[2]) <= 21
        ) :
            drawCard(house, True)
            printCards(args[0], args[1], args[2], args[3], args[4])
    return printWinner()

def printCards(*args):
    if args[0] != True:
        if calculateScore(house) == 21 or dealerMove == True:
            printHouseCardsUp()
            printPlayerCards()
        else:
            printHouseCardsDown()
            printPlayerCards()
    else:
        if calculateScore(house) == 21 or dealerMove == True:
            printHouseCardsUp()
            splitPrint(args[1], args[2], args[3], args[4])
        else:
            printHouseCardsDown()
            splitPrint(args[1], args[2], args[3], args[4])

def spliting(handOne, handTwo,bet):
    split = True
    printHandOne = True
    printCards(split, handOne, handTwo, printHandOne, bet)
    while calculateScore(handOne) < 21:
        print("HAND 1 - H-hit |\t L-stand |\t ")
        playerInput = input("-")
        if playerInput.lower() == "h":
            drawCard(handOne,False)
            printCards(split, handOne, handTwo, printHandOne, bet)
        elif playerInput.lower() == "l":
            break
        else:
            print("Not valid input!")
    printHandOne = False
    while calculateScore(handTwo) < 21:
        print("HAND 2 - H-hit |\t L-stand |\t ")
        playerInput = input("-")
        if playerInput.lower() == "h":
            drawCard(handTwo,False)
            printCards(split, handOne, handTwo, printHandOne, bet)
        elif playerInput.lower() == "l":
            break
        else:
            print("Not valid input!")

    return True, printHandOne
def resetAces():
    for i in shuffledDeck:
        if i["name"] == "ace":
            i["value"] = 11
"""
Things I need to do:
I think i need to remake print functions or make a new function that takes in cards and transformes them into actual cards
"""
# Main game loop
money = 500
shuffledDeck = shuffle()
run = True
while run:
    printHandOne = True
    player = []
    house = []
    move = 0
    dealerMove = False
    playerInput = ""
    bet = 0
    split = False
    if len(shuffledDeck) < 15:
        print("Changing the deck")
        resetAces()
        shuffledDeck = shuffle()
    print("Input | p to play \n q to quit")
    playerInput = input("-")
    if playerInput.lower() == "p":
        while(True and run):
            try:
                playerInput = int(input("PLACE YOUR BET, YOU HAVE {} $ \n-".format(money)))
                if money - playerInput < 0:
                    print("YOU DONT HAVE ENOUGH FUNDS")
                    print("YOU CAN ADD MORE MONEY OR STOP PLAYING(add or stop)")
                    while(True):
                        inputMode = input("-")
                        if(inputMode.lower() == "add"):
                            while(True):
                                try:
                                    inputMoney = int(input("HOW MUCH MONEY DO YOU WANT TO DEPOSIT? \n-"))
                                    if(money + inputMoney < playerInput ):
                                        print("ADD THE RIGHT AMOUNT TO MATCH THE BET")
                                        continue
                                except:
                                    ("INPUT A NUMBER!")
                                else:
                                    money += inputMoney
                                    break
                            break
                        elif(inputMode.lower() == "stop"):
                            run = False
                            break
                        else:
                            print("NOT VALID INPUT (add or stop)")
            except:
                print("INPUT A NUMBER!")
            else:
                bet = playerInput
                money -= playerInput
                break
        if not run:
            break
        dealCards()
        if aces(player) and calculateScore(player) != 21:
            split, handOne, handTwo, printHandOne, dealerMove, money, bet = checkPlayerCards(player, money, bet)
        #There was a split condition in this loop
        while calculateScore(player) < 21 and dealerMove != True:
            print(len(shuffledDeck))
            if (
                player[0]["name"] == player[1]["name"]
                and player[0]["value"] == player[1]["value"]
            ):
                if move == 0:
                    print("S-split |\t H-hit |\t L-stand |\t D - double down |")
                else:
                    print("S-split |\t H-hit |\t L-stand |")
                playerInput = input("-")
                if playerInput.lower() == "s":
                    if money - bet >= 0:
                        money -= bet
                        bet += bet
                        handOne = [player[0]]
                        handTwo = [player[1]]
                        dealerMove, printHandOne = spliting(handOne, handTwo, bet)
                        split = True
                    else:
                        print("YOU DONT HAVE ENOUGH MONEY :()")
                elif playerInput.lower() == "h":
                    drawCard(player, False)
                    printCards(split)
                    move+=1
                elif playerInput.lower() == "d" and move == 0:
                    if money - bet * 2 >= 0:
                        money -= bet
                        bet += bet
                        drawCard(player, False)
                        printCards(split)
                        dealerMove = True
                    else:
                        print("YOU DONT HAVE ENOUGH MONEY :()")
                elif playerInput.lower() == "l":
                    dealerMove = True
                    break
                else:
                    print("Not valid input!")
            else:
                if move == 0:
                    print("H-hit |\t L-stand |\t D - double down |")
                else:
                    print("H-hit |\t L-stand |")
                playerInput = input("-")

                if playerInput.lower() == "h":
                    drawCard(player, False)
                    printCards(split)
                    move+=1
                elif playerInput.lower() == "d" and move == 0:
                    if money - bet >= 0:
                        money -= bet
                        bet += bet
                        drawCard(player, False)
                        printCards(split)
                        dealerMove = True
                    else:
                        print("YOU DONT HAVE ENOUGH MONEY :()")
                elif playerInput.lower() == "l":
                    dealerMove = True
                    break
                else:
                    print("Not valid input!")
        if calculateScore(player) >= 21:
            dealerMove = True
        if split:
            money += dealersMove(split, handOne, handTwo, printHandOne, bet)
        else:
            money += dealersMove(split)
        player.clear()
        house.clear()
    elif playerInput.lower() == "q" or not run:
        break
    else:
        print("\nNot valid input! \n")