class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def get_value(self):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10,
                  'King': 10, 'Ace': 11}
    return values[self.value]
  
  def __str__(self):
    # returns readable string representation of a card
    return f"{self.value} of {self.suit}"
  
  def __eq__(self, other):
    # comparesa current card object with another card object
    return self.suit == other.suit and self.value == other.value


  