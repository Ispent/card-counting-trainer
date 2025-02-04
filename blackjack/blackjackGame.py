'''
patty lee
blackjack game
'''

'''
!!! i have no idea why right now but something kinda broke when I busted and the dealer's turn went anyways so reminder to fix !!!
wait this might be more broken than i had realized
'''


import os
import sys

cwd = os.getcwd()
sub_cwd = os.path.join(cwd, "..")
sys.path.append(sub_cwd)

from player import Player
from deck import Deck, Card


class BlackjackGame:
  def __init__(self, name='Player'):
    '''uhhhh''' 
    # initializes with the trash player and the two player objects, does both this class and initialized deck need to be here?
    self.trashPile = Deck()

    self.player = Player(name)
    self.dealer = Player("Dealer", is_dealer=True)

  def __len__ (self):
    # length
    return len(self.deck)
    

  def initialize_deck(self, deckCount=1): # the name of this is like literally the same thing as below
    # creates the deck that will be used during play
    # do people even get to choose and/or should that even be a function of the program???
    self.deck = Deck()
    self.deck.add_deck(deckCount)
    self.deck.shuffle()
    return self.deck

  def deal_initial(self): # see above comment on name redundancy lol (but they different)
    # deals both the player and the dealer 2 cards, each going one card at a time
    for card in range(2):
      self.player.add_card(self.deck.peek())
      self.deck.cards.pop(0)
      self.dealer.add_card(self.deck.peek())
      self.deck.cards.pop(0)

  def deal(self, recepient):
    # again the name is like super boring and potentially even redundant but like ugh
    if len(self.deck.cards) == 0:
      # just in case deck happens to run out mid game (should be impossible currently... ....... :(
      print("The deck is empty. Adding more cards to the deck")
      self.deck.add_deck()
      self.deck.shuffle()
      # again with the high-key confusing ass class names
        
    card = self.deck.peek()
    print(f"{recepient.name} has drawn {card}")
    recepient.add_card(card)
    self.deck.cards.pop(0)

  def player_turn(self): # the first and every other consequent round !!
    # if the dealer were to start with 21, automatically end game without progressing --> yes i must do this
    # idk how this works rn that well too tired


    self.dealer.calculate_score()
    self.player.calculate_score()


    # like surely i coud consolidate all of this and have it be like prelim check
    # 

    if self.check_immediate_win():
      return

    # its yo turn
    print(f"\n{self.player.name}'s Turn\n")
    print (self.player.display_hand())


    # logic behind hitting and standing ---> i guess this is fine??
    while not self.player.is_busted():
      print(self.dealer.display_hand())
    
      choice = input('\nWould you like to hit or stand (h/s): ').strip().lower()
      while choice not in ('h', 's'):
        choice = input("Invalid input. Enter 'h' or 's': ").strip().lower()


      if choice == 'h':
        self.deal(self.player)
        print(self.player.display_hand())
        self.player.calculate_score()

        if self.check_immediate_win():
          return
      
      elif choice == 's':
        print(f"{self.player.name} will stand.\n")
        break



  def dealer_turn(self):
    '''dealer object will draw cards until their score is a hard 17'''
    print("Dealer's Turn\n")
    print(self.dealer.display_hand(show_all=True))

    while self.dealer.calculate_score() < 17:
      self.deal(self.dealer)
    

    if self.dealer.is_busted():
      print("Dealer Busts, You win!")
      return 

    self.final_winner_check()
    
  
  def soft_sixteen_check(self):
    # again with perchance questionable implementation, but i guess I could reuse this code at some point for the cpu thingie thingie 
    # --> *update: ?? I mean when there is an ace present and I need to check to see if there is room to be able to draw another
    # but like should i even or is there som better
    dealer_score = self.dealer.calculate_score()

    if dealer_score >= 17 and self.dealer.aces and self.dealer.is_dealer == True:
        dealer_score -= 10
        self.dealer.aces -= 1
    self.dealer.score = dealer_score
  

  def check_immediate_win(self):
    # i shoud write this
    # prelim natural 21 check :D finally !!!
    if self.dealer.is_natural() and self.player.is_natural():
      print ("\nTie!")
      return True

    elif self.dealer.is_natural():
      print( "\nDealer has Blackjack, you lost" )
      return True
    
    elif self.player.is_natural():
      print( "\nPlayer has Blackjack, you won!")
      return True
    
    elif self.player.is_busted():
      print( "\nYou Busted")
      return True
    
    return False
  
  def final_winner_check(self):
    '''in the end of a round, will check who the winner is'''
    player_score = self.player.calculate_score()
    dealer_score = self.dealer.calculate_score()

    if player_score > dealer_score:
      print("\nPlayer wins!")
    elif dealer_score > player_score:
      print("\nDealer Wins!")
    else:
      print("\ntie!")
    
  def end_round(self):
    '''given the end of the round, will clean the 
      current hand and add to discard file'''
    self.trashPile.cards.extend(self.player.hand)
    self.trashPile.cards.extend(self.dealer.hand)

    self.player.hand.clear()
    self.dealer.hand.clear()

    while True:
      replay = input("Would you like to play again? (y/n): ")

      if replay == 'y':
        self.deal_initial()
        self.player_turn()
        if not self.player.is_natural():
          self.dealer_turn()

      
      elif replay == "n":
        exit()

      else:
        print("Invalid input please try again")


  def deck_input_check(self):
    '''ensures the input is in int format'''
    while True:
      try:
        deckCount = int(input("How many decks would you like to use?: "))
        return deckCount
      except ValueError:
        print("Invalid input. Please enter an integer")
      if isinstance(deckCount, int) and 20 > deckCount > 0:
        break

    return deckCount
    
  def start_game(self):
    # start da game
    deckCount = self.deck_input_check()
    self.deck = self.initialize_deck(deckCount)
    self.deal_initial()
    self.player_turn()

    if not self.player.is_natural():
      self.dealer_turn()

    self.end_round()



if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()