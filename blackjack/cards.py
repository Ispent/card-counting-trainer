class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
  
  def __str__(self):
    # returns readable string representation of a card
    return f"{self.value} of {self.suit}"
  
  def __eq__(self, other):
    # comparesa current card object with another card object
    return self.suit == other.suit and self.value == other.value


  