class Player:
  def __init__(self, name, is_dealer=False):
    self.name = name
    self.hand = []
    self.is_dealer = is_dealer
    self.score = 0
    self.aces = 0

  def add_card(self, card):
    # add a card to the player's hand
    self.hand.append(card)

  def calculate_score(self):
    # calculate the score in the current hand, accounting for aces
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10,
                  'King': 10, 'Ace': 11}
    score = 0
    aces = 0

    for card in self.hand:
      score += values[card.value]
      if card.value == "Ace":
        aces += 1
    
    while score > 21 and aces:
      score -= 10
      aces -= 1

    self.score = score
    return score

  def is_busted(self):
    self.calculate_score()
    
    # after calculating the score, show if player busts
    return self.score > 21
    
  def is_natural(self):
    # after calculating score, show if player wins
    if self.score == 21:
      return True

  def display_hand(self, show_all=False):
    # display the current hand, if you are a dealer and show_false is flagged as false, only show the first card --> else just show all
    if show_all == False and self.is_dealer == True:
      return f"Dealer's hand is a {self.hand[0]} and [Hidden Card]"
    
    if len(self.hand) > 1:
        hand_str = ', '.join(str(card) for card in self.hand[:-1]) + f", and {self.hand[-1]}"
    else:
        hand_str = str(self.hand[0])
    return f"{self.name}'s hand is a {hand_str}"

  def reset_hand(self):
    # reset's player hand to nothin
    self.hand = []