# import Card class
import Card

# import random module
import random

# create standard deck of 52 cards
deck = [x for x in range(52)]

# initialize list of card objects
cards = []

# create 52 card objects from deck
for x in deck:
    cards.append(Card.Card(x))

# shuffle the deck
random.shuffle(cards)

# getCard for first 4 cards in shuffled deck
for i in range(4):
    cards[i].getCard()
