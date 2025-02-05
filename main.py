from nicegui import ui
from blackjackGame import BlackjackGame

game = BlackjackGame()
def update_deck_count(deckCount):
    game.initialize_deck(deckCount)

ui.number(label='Decks', value=1, format='%d', on_change=lambda e: update_deck_count(int(e.value)))

ui.run()
