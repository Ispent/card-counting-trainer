# things to do
# need to implement a way to determine the value of a card when pulled
# do i need error handling???? 
# add actual value implementation for Jack, Queen, King and Ace in Card object
# how tf do i make the ace be worth 1 or 11

from cards import Card
import itertools
import random

class Deck:
  suitList = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
  valueList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] # is ace first or last in a deck ???? # does it even matter ????

  def __init__(self):
    self.cards = []

  def add_deck(self, deckCount=1):
    # automatically populates the list with cards, with support for multiple decks
    # by default will contain 1 deck of 52 cards
    self.deckCount = deckCount

    for suit, value in itertools.product(self.suitList, self.valueList):
      for i in range(0, deckCount):
        self.cards.append(Card(suit, value))

  def add_card(self, card):
    # adds a card object to the list
    self.cards.append(card)

  def clear_deck(self):
    # clears the list of all card objects
    self.cards = []

  def discard(self, amount=1): # logic so u cant remove more cards then the total 
    # discards specified amount of cards from the top of the deck 
    # by default will remove the first card
    self.cards = self.cards[amount:]

  def shuffle(self):
    # uses random module to shuffle the list (deck)
    random.shuffle(self.cards)
  
  def peek(self, index=0): # add error handling (?)
    # returns the top card in the deck
    return self.cards[index]


  def __str__(self):
    # returns a readable representaion of all the cards separated by commmas
    return ', '.join(str(card) for card in self.cards)
  
  def __len__(self):
    # returns the length of the deck list (or how many cards there are ??)
    return len(self.cards)

  
