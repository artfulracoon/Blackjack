import random
import time
import os
import msvcrt

bank = 1000
bankBeforeBet = 0
cardsInDeck = 52

deck = ['K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J', 'A', 'A', 'A', 'A', 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7,
        6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]
playerHand = []
dealerHand = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def reinitiateVars():
    global deck, playerHand, dealerHand, cardsInDeck
    deck = ['K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J', 'A', 'A', 'A', 'A', 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7,
            7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]
    playerHand = []
    dealerHand = []
    cardsInDeck = 52


def showHand(somelist):
    for obj in somelist:
        print(obj, end=" ")
    print(" ")


def sumOfHand(someList):
    localsum = 0
    localcheckace = 0
    for obj in someList:
        if obj == 'K' or obj == 'Q' or obj == 'J':
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
                localcheckace -= 1
    return localsum


def takeBets():
    def betInputCaller():

        print("Current bet: " + str(currentBet) + "\n")
        print("You have " + str(bank) +
              "$ in the bank. How much do you want to bet?\n")
        print(
            "1. 5 \n2. 10 \n3. 50 \n4. 100 \n5. 500 \n6. 1000\n\n9. Revert\n0. Continue\n")
        try:
            theInput = int(msvcrt.getch())
        except ValueError:
            clear()
            print("Wrong value input! Please try again:")
            print(
                "1. 5 \n2. 10 \n3. 50 \n4. 100 \n5. 500 \n6. 1000\n\n9. Revert\n0. Continue\n")
            theInput = int(msvcrt.getch())
        while betInput not in [0, 1, 2, 3, 4, 5, 6, 9]:
            clear()
            print("Current bet: " + str(currentBet) + "\n")
            print("Wrong Input! Please state your bet according to: ")
            print(
                "1. 5 \n2. 10 \n3. 50 \n4. 100 \n5. 500 \n6. 1000\n\n9. Revert\n0. Continue\n")

            theInput = int(msvcrt.getch())
        return theInput

    global bank
    currentBet = 0
    betInput = 1
    while betInput != 0:

        betInput = betInputCaller()

        if betInput == 1:
            betCurrent = 5
        elif betInput == 2:
            betCurrent = 10
        elif betInput == 3:
            betCurrent = 50
        elif betInput == 4:
            betCurrent = 100
        elif betInput == 5:
            betCurrent = 500
        elif betInput == 6:
            betCurrent = 1000
        elif betInput == 9:
            if currentBet == 0:
                clear()
                print("You cannot bet below zero!")
                time.sleep(1.5)
                currentBet -= betCurrent
            else:
                currentBet -= betCurrent*2

        currentBet += betCurrent
        if currentBet > bank:
            currentBet -= betCurrent
            clear()
            print("Your bet cannot exceed your bank!")
            time.sleep(1.5)
        clear()
    return currentBet


def chooseCard():
    global deck, cardsInDeck
    someNumber = random.randint(0, cardsInDeck-1)
    card = deck[someNumber]
    deck.remove(card)
    cardsInDeck -= 1
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
        global bet, playerHand
        choiceLocal1 = int(
            input("\nHit, Stand or Double ?\n1. Hit\n2. Stand\n"))
        sumsum1 = sumOfHand(playerHand)

        if sumsum1 == 21:
            return 2
        elif sumsum1 > 21:
            return 0

        if choiceLocal1 == 1:
            clear()
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
            clear()
            print("You have chosen to stand.\n")
            return

    global bet, playerHand

    sumsum = sumOfHand(playerHand)

    if sumsum == 21:
        return 2

    elif sumsum > 21:
        return 0

    choiceLocal = int(
        input("\nHit, Stand or Double ?\n1. Hit\n2. Stand\n3. Double\n"))

    if choiceLocal == 1:
        clear()
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
        clear()
        print("You have chosen to stand.")
        return

    else:
        clear()
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
    global bank, bet, playerHand, dealerHand
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
        print("Your hand:", end=" ")
        showHand(playerHand)
        print("You have won with a blackjack!")
        bank += int(bet*1.5)
    else:
        time.sleep(1)
        dealersResult = dealerTurn()
        if dealersResult == 0:
            print("The house has gone bust. You have won.")
            bank += bet
        else:
            if sumOfHand(playerHand) == sumOfHand(dealerHand):
                print("It is a tie. The bet is off.")
                bank = bankBeforeBet
            elif sumOfHand(playerHand) > sumOfHand(dealerHand):
                print("Your hand:", end=" ")
                showHand(playerHand)
                print("You have won.")
                bank += bet
            else:
                print("Your hand:", end=" ")
                showHand(playerHand)
                print("You have lost.")
                bank -= bet


playAgain = 1
while playAgain == 1:
    clear()
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
