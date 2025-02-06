from nicegui import ui
from blackjackGame import BlackjackGame

game = BlackjackGame()
deck_count = 1

def update_deck_count(deckCount):
    global deck_count 
    deck_count = deckCount
    game.initialize_deck(deckCount)

def init_deck():
    game.initialize_deck(deck_count)
    game.deal_initial()

ui.number(label='Decks', value=1, format='%d', on_change=lambda e:  update_deck_count(int(e.value)) if e.value and int(e.value) > 0 else None )
ui.button("Start Game", on_click=lambda: init_deck())

ui.run()
