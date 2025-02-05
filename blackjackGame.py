'''
patty lee
blackjack game
'''

'''
!!! i have no idea why right now but something kinda broke when I busted and the dealer's turn went anyways so reminder to fix !!!
wait this might be more broken than i had realized
'''

''' hopefully this is allowing for the code be the run from command line if thats even important at all becuase of my funky folder setup'''
import os
import sys

cwd = os.getcwd()
sub_cwd = os.path.join(cwd, "..")
sys.path.append(sub_cwd)

from player import Player
from deck import Deck


class BlackjackGame:
  def __init__(self, name='Player'):
    '''Class representing the gamestate of a round of blackjack(?)
    
    parameter:
      name (str): name of the player
      trashPile (Deck): Deck object used to keep track of discarded cards
      player (player): player object representing the human player 
      dealer (player): player object representing the dealer, with built in flag for the player class
    ''' 
    # initializes with the trash player and the two player objects, does both this class and initialized deck need to be here?
    self.trashPile = Deck()
    self.player = Player(name)
    self.dealer = Player("Dealer", is_dealer=True)

  def __len__ (self):
    # length
    return len(self.deck)
    

  def initialize_deck(self, deckCount=1):
    '''
    initializes the deck object by adding the cards and shuffling them

    Args:
      deckCount(int): keeps track of number of decks being used
        - defaults to 1 deck, internally limited to 20 decks total

    returns:
      deck (Deck): Returns the shuffled deck 
    '''
    
    self.deck = Deck()
    self.deck.add_deck(deckCount)
    self.deck.shuffle()
    return self.deck

  def deal_initial(self): 
    '''
    acts as the start of every "round" and deals two cards each all players
    '''
    # logically flawed function lowkey no>??
    # hard baked in two player lock
    # maybe make like a loop so we can just deal 2 cards to every player
    # at some point......

    for card in range(2):
      self.player.add_card(self.deck.peek())
      self.deck.cards.pop(0)
      self.dealer.add_card(self.deck.peek())
      self.deck.cards.pop(0)

  def deal(self, recepient):
    # again the name is like super boring and potentially even redundant but like ugh
    
    # wait i just realized this deal function also doesnt really work allat well 
      # make sure to fix the fact that my function to add more cards to the deck doesnt 
      # actually take the cards from the discard pile but grabs a new deck instead
    '''
    deals one card to a specified recepient

    Args:
      recipient (Player): the player object that will receive the card
    '''

    if len(self.deck.cards) == 0:
      # just in case deck happens to run out mid game (should be impossible currently... ....... :(
      # fix this !!!!
      print("The deck is empty. Adding more cards to the deck")
      self.deck.add_deck()
      self.deck.shuffle()
        
    card = self.deck.peek()
    print(f"{recepient.name} has drawn {card}")
    recepient.add_card(card)
    self.deck.cards.pop(0)

  def player_turn(self): 
    '''
    manages the flow of the player's turn in a round
      - Calculates player and dealer's score
      - if either player acheives an automatic win, will appropirately end the game
    
    '''

    self.dealer.calculate_score()
    self.player.calculate_score()

    # like im 99% certain that this does not work as intended ---> im 99% certain i fixed it now
    if self.check_immediate_win():
      return
    
    print(f"\n{self.player.name}'s Turn\n")
    print (self.player.display_hand())


    # logic behind hitting and stanifding ---> i guess this is fine??
    while not self.player.is_busted():
      print(self.dealer.display_hand())
    
      choice = input('\nWould you like to hit or stand (h/s): ').strip().lower()

      if choice == 'h':
        self.deal(self.player)
        self.player.calculate_score()
        if self.check_immediate_win():
          return
        
      elif choice == 's':
        break
      else:
        print("Invalid choice. Please enter 'h' to hit or 's' to stand.")

      print(f"\n{self.player.name}'s turn is over.\n")


  def dealer_turn(self):
    '''
    manages the flow of the dealer's turn
      - dealer will keep drawing cards until they hit a score of hard 17 or bust 
    '''

    print("Dealer's Turn\n")
    print(self.dealer.display_hand(show_all=True))

    while self.dealer.calculate_score() < 17:
      self.deal(self.dealer)
      self.soft_sixteen_check()
    

    if self.dealer.is_busted():
      print("Dealer Busts, You win!")
      return 

    self.final_winner_check()
    
  
  def soft_sixteen_check(self):
    '''
    Adjusts the dealer's score if they were to be holding onto a soft 17 (17 with an ace as 11)

    Will subtract 10 points for every ace in the hand, as long as the hand score reamains above 17, and the player object contains dealer flag
    '''

    # again with perchance questionable implementation, but i guess I could reuse this code at some point for the cpu thingie thingie 
    # --> *update: ?? I mean when there is an ace present and I need to check to see if there is room to be able to draw another
    # but like should i even or is there som better

    dealer_score = self.dealer.calculate_score()

    while dealer_score >= 17 and self.dealer.aces > 0 and self.dealer.is_dealer:
        dealer_score -= 10
        self.dealer.aces -= 1
        self.dealer.score = dealer_score
  

  def check_immediate_win(self):
    '''
    At certain points in the game, will check for immediate win conditions as a result of an action, instead of the natural end of round

    Checks to see if either player object's score is exactly 21 or higher, and if satisfired will end the game immediately

    returns: 
      bool: True if immediate win/loss condition is met, false if not
    '''

    # i shoud write this
    # prelim natural 21 check :D finally !!!
    # where tf do i calculate scores
      # i should have started writing these comments earlier
    if self.dealer.is_natural() and self.player.is_natural():
      print ("\nTie!")
      self.end_round()
      return True

    elif self.dealer.is_natural():
      print( "\nDealer has Blackjack, you lost" )
      self.end_round()
      return True
    
    elif self.player.is_natural():
      print( "\nPlayer has Blackjack, you won!")
      self.end_round()
      return True
    
    elif self.player.is_busted():
      print( "\nYou Busted")
      self.end_round()
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

    if self.player.is_natural():
      self.end_round()

    self.dealer_turn()
    self.end_round()



if __name__ == "__main__":
    game = BlackjackGame()
    game.start_game()