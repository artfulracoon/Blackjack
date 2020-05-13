import random
import time
import os

bank = 1000
bankBeforeBet = 0
card = 0


deck = ['K', 'K', 'K', 'Q', 'Q', 'Q', 'A', 'A', 'A', 10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 7, 7,
        6, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2]
playerHand = []
dealerHand = []


def reinitiateVars():
    global deck
    global playerHand
    global dealerHand
    deck = ['K', 'K', 'K', 'Q', 'Q', 'Q', 'A', 'A', 'A', 10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 7, 7,
            6, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2]
    playerHand = []
    dealerHand = []


def showHand(somelist):
    for obj in somelist:
        print(obj, end=", ")
    print(" ")


def sumOfHand(someList):
    localsum = 0
    localcheckace = 0
    for obj in someList:
        if obj == 'K' or obj == 'Q':
            obj = 10
        elif obj == 'A':
            if localsum + 11 > 21:
                obj = 1
            else:
                localcheckace += 1
                obj = 11
        localsum += obj
        if localsum > 21 and localcheckace != 0:
            for i in range(localcheckace):
                localsum -= 10
    return localsum


def takeBets():
    global bank
    global bet
    bet = int(input("You have " + str(bank) +
                    "$ in the bank. How much do you want to bet?\n"))
    while bet > bank or bet <= 0:
        takeBets()
    return bet


def chooseCard():
    global deck, card
    someNumber = random.randint(1, 43)
    try:
        card = deck[someNumber]
    except:
        chooseCard()
    deck.remove(card)
    return card


def dealHand(mylist):
    for i in range(2):
        cardChosen = chooseCard()
        mylist.append(cardChosen)


def dealerTurn():
    global dealerHand
    print("The dealer's hand consists of: ", end=" ")
    showHand(dealerHand)
    sumsum = sumOfHand(dealerHand)

    if sumsum > 21:
        return 0
    elif sumsum == 21:
        return 1
    elif 21 > sumsum > 17:
        return 1
    elif sumsum < 17:
        chosenCard1 = chooseCard()
        print("\nThe dealer draws a card: " + str(chosenCard1))
        dealerHand.append(chosenCard1)
        print("New sum is: " + str(sumOfHand(dealerHand)))
        return dealerTurn()


def playerTurn():
    def playerTurnNoDouble():
        global bet
        global playerHand
        choiceLocal1 = int(
            input("\nHit, Stand or Double ?\n1. Hit\n2. Stand\n"))
        sumsum1 = sumOfHand(playerHand)

        if sumsum1 == 21:
            return "\nYou have won this round with a blackjack."
        elif sumsum1 > 21:
            return 0

        if choiceLocal1 == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You have chosen to hit.\n")
            cardChosen1 = chooseCard()
            playerHand.append(cardChosen1)
            print("You draw the card: " + str(cardChosen1))
            print("Your hand:", end=" ")
            showHand(playerHand)
            print("Your new sum is: " + str(sumOfHand(playerHand)) + "\n")
            if sumOfHand(playerHand) > 21:
                return 0
            else:
                return playerTurnNoDouble()

        elif choiceLocal1 == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You have chosen to stand.\n")
            return

    global bet
    global playerHand

    sumsum = sumOfHand(playerHand)

    if sumsum == 21:
        return 2

    elif sumsum > 21:
        return 0

    choiceLocal = int(
        input("\nHit, Stand or Double ?\n1. Hit\n2. Stand\n3. Double\n"))

    if choiceLocal == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have chosen to hit.\n")
        cardChosen = chooseCard()
        playerHand.append(cardChosen)
        print("You draw the card: " + str(cardChosen))
        print("Your hand:", end=" ")
        showHand(playerHand)
        print("Your new sum is: " + str(sumOfHand(playerHand)) + "\n")
        if sumOfHand(playerHand) > 21:
            return 0
        if playerTurnNoDouble() == 0:
            return 0

    elif choiceLocal == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have chosen to stand.")
        return

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have chosen to double down. Good luck.")
        bet = bet * 2
        chosenCard2 = chooseCard()
        playerHand.append(chosenCard2)
        if sumOfHand(playerHand) > 21:
            print("You draw the card: " + str(chosenCard2))
            print("Your hand:", end=" ")
            showHand(playerHand)
            print("Your new sum is: " + str(sumOfHand(playerHand)) + "\n")
            return 0


def gameStart():
    global bank
    global bet
    global playerHand
    global dealerHand
    dealHand(dealerHand)
    dealHand(playerHand)
    print("\nDealer's hand: " + str(dealerHand[0]) + " and one face down")
    print("Your hand:", end=" ")
    showHand(playerHand)
    print("Your cards sum up to: " + str(sumOfHand(playerHand)))
    conclusion = playerTurn()
    if conclusion == 0:
        print("Your hand consists of: ", end=" ")
        showHand(playerHand)
        print("You have busted. Damn.")
        bank -= bet
    elif conclusion == 2:
        print("You have won with a blackjack!")
        bank += bet
    else:
        time.sleep(1)
        dealersResult = dealerTurn()
        if dealersResult == 0:
            print("The house has gone bust. You have won.")
            bank += bet*2
        else:
            if sumOfHand(playerHand) == sumOfHand(dealerHand):
                print("It is a tie. The bet is off.")
                bank = bankBeforeBet
            elif sumOfHand(playerHand) > sumOfHand(dealerHand):
                print("You have won.")
                bank += bet*2
            else:
                print("You have lost.")
                bank -= bet


playAgain = 1
while playAgain == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    bankBeforeBet = bank
    bet = takeBets()
    time.sleep(1)
    gameStart()
    reinitiateVars()
    if bank <= 0:
        print("Your current money status: " + str(bank))
        print("You don't have any more money to bet. Gambling is really a hell of a drug.")
        break
    playAgain = int(input("\nWanna try your luck again? \n1. Yes \n2. No\n"))
