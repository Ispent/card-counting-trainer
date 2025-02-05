import pytest
from deck import Deck
from cards import Card
from player import Player
from blackjackGame import BlackjackGame

class TestDeck:

  def test_addToDeck(self):
    # tests adding card object to deck
    deck = Deck()
    card = Card("Hearts", "2")
    deck.add_card(card)
    assert len(deck) == 1
    assert deck.peek() == card
    
  def test_createDeck(self):
    # testing the deck establishemnt (lowkey do i just put this in init ??)  -->  maybe do like Deck(num of decks)
    deck = Deck()
    deck.create_deck(1)
    assert len(deck) == 52
    
    deck2 = Deck()
    deck2.create_deck(2)
    assert len(deck2) == 104

  def test_clearDeck(self):
    # tests the fnction to clear out da deck 
    deck = Deck()
    deck.create_deck(1)
    deck.clear_deck()
    assert len(deck) == 0

  def test_shuffleDeck(self):
    # tests the shuffle by comparison with an identical deck --> but also if i try it enough this test fails in theory ???
    # is this even a meaningful way to test this >?
    deck = Deck()
    deck2 = Deck()

    deck.create_deck()
    deck2.create_deck()
    deck2.shuffle()

    assert deck != deck2

  def test_discardDeck(self):
    # discard da cardtest_start_game
    deck = Deck()
    deck.create_deck()

    deck.discard()
    assert len(deck) == 51

    deck.discard(5)
    assert len(deck) == 46



class TestCard:
  
  def test_cardEquivalence(self):
    card = Card("Hearts", "King")
    card2 = Card("Hearts", "King")

    card3 = Card("Hearts", "6")
    card4 = Card("Spades", "King")
    card5 = Card("Diamonds", "2")

    # these two cards are da same and should report so
    assert card == card2
    
    # these cards got the same suit but diff values
    assert card != card3

    # these cards got the same value but diff suit
    assert card != card4

    # these cards are for sure different from each other
    assert card != card5


  
class TestPlayer:

  def test_playerAdd(self):
    card = Card("Hearts", "King")
    player1 = Player("patty")

    player1.add_card(card)
    
    assert player1.hand[0] == card

  def test_playerCalculateScore(self):
    card = Card("Hearts", "King")
    card2= Card("Spades", "Ace")
    player1 = Player("patty")

    player1.add_card(card)
    player1.add_card(card2)

    assert player1.calculate_score() == 21


  def test_playerIsBusted(self):
    card = Card("Hearts", "King")
    card2= Card("Spades", "9")
    card3 = Card("Spades", "5")
    player1 = Player("patty")

    player1.add_card(card)
    player1.add_card(card2)
    player1.add_card(card3)

    player1.calculate_score()
    assert player1.is_busted()

    card4 = Card("Hearts", "King")
    card5 = Card("Spades", "9")
    player2 = Player("patty")

    player2.add_card(card4)
    player2.add_card(card5)

    player2.calculate_score()
    assert not player2.is_busted()


    card6 = Card("Hearts", "King")
    card7 = Card("Spades", "Ace")
    card8 = Card("Spades", "Jack")
    card9 = Card('Clubs', '2')
    player3 = Player("patty")
    player3.calculate_score()

    player3.add_card(card6)
    player3.add_card(card7)
    player3.add_card(card8)
    player3.add_card(card9)

    player3.calculate_score()
    assert player3.is_busted()

  def test_is_natural(self):
    card = Card("Hearts", "King")
    card2 = Card("Spades", "Ace")
    player = Player('Patty')

    player.add_card(card)
    player.add_card(card2)
    player.calculate_score()

    assert player.is_natural()

  def test_display_hand(self):
    card = Card("Hearts", "King")
    card2= Card("Spades", "9")
    card3 = Card("Spades", "5")
    player1 = Player("patty", True)

    player1.add_card(card)
    player1.add_card(card2)
    player1.add_card(card3)

    assert player1.display_hand() == "Dealer's hand is a King of Hearts and [Hidden Card]"

    
    card4 = Card("Hearts", "King")
    card5= Card("Spades", "9")
    card6 = Card("Spades", "5")
    player2 = Player("patty", is_dealer=True)

    player2.add_card(card4)
    player2.add_card(card5)
    player2.add_card(card6)
    assert player2.display_hand(True) == "patty's hand is a King of Hearts, 9 of Spades, and 5 of Spades"

    
class TestBlackjackGame:

  def test_initialize_deck(self):
    game = BlackjackGame("patty")
    game.initialize_deck(2)
    assert len(game.deck) == 104

  def test_deal_initial(self):
    game = BlackjackGame("patty")
    game.initialize_deck(1)
    game.deal_initial()

    player_hand = game.player.display_hand()
    dealer_hand = game.dealer.display_hand()

    assert len(game.player.hand) == 2
    assert len(game.dealer.hand) == 2
    assert "patty's hand is a" in player_hand
    assert "Dealer's hand is a" in dealer_hand

    
  def test_soft_sixteen_check(self):
    game = BlackjackGame()
    dealer = Player("Dealer", is_dealer=True)
    dealer.hand = [Card("Hearts", "Ace"), Card("Spades", "6")]
    game.dealer = dealer
    game.soft_sixteen_check()
    assert game.dealer.score == 7
    assert game.dealer.aces == 0 
    

# not pytest idk even how to test this easily

game = BlackjackGame('Patty')
game.start_game()

