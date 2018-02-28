# Module that defines the Card class with datafields suit and rank. Contains methods getSuit, getRank, and getCard which return
# card suit, card rank, and print the rank and suit, respectively.

# create card class
class Card:
    def __init__(self, cardNumber):
        self.__suit = cardNumber // 13
        self.__rank = cardNumber % 13

# define method that returns suit of card as a string
    def getSuit(self):
        if self.__suit == 0:
            return "hearts"
        elif self.__suit == 1:
            return "diamonds"
        elif self.__suit == 2:
            return "spades"
        else:
            return "clubs"

# define method that returns rank of card as a string
    def getRank(self):
        if self.__rank == 0:
            return "two"
        elif self.__rank == 1:
            return "three"
        elif self.__rank == 2:
            return "four"
        elif self.__rank == 3:
            return "five"
        elif self.__rank == 4:
            return "six"
        elif self.__rank == 5:
            return "seven"
        elif self.__rank == 6:
            return "eight"
        elif self.__rank == 7:
            return "nine"
        elif self.__rank == 8:
            return "ten"
        elif self.__rank == 9:
            return "jack"
        elif self.__rank == 10:
            return "queen"
        else:
            return "king"

# define method for printing rank and suit of card
    def getCard(self):
        print(self.getRank(), "of", self.getSuit())
