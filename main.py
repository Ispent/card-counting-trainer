from nicegui import ui
from blackjackGame import BlackjackGame


class blackjackGui:
    def __init__(self):
        self.game = BlackjackGame()
        self.deck_count = 1
        self.player_score = None
        self.dealer_score = None
        

    def update_deck_count(self, deckCount):
        self.deck_count = deckCount
        self.game.initialize_deck(deckCount)

    def init_deck(self):
        self.game.initialize_deck(self.deck_count)
        self.game.deal_initial()
        self.player_score.set_value(self.game.player.display_hand())
        self.dealer_score.set_value(self.game.dealer.display_hand())

    def create_ui(self):        

        ui.number(label='Decks', value=1, format='%d', on_change=lambda e:  self.update_deck_count(int(e.value)) if e.value and int(e.value) > 0 else None)
        self.player_score = ui.input(label='Player Hand', value=0,).props("readonly").style('auto-width')
        self.dealer_score = ui.input(label='Dealer Hand', value=0,).props("readonly").classes('auto-width')


        ui.button("Start Game", on_click=lambda: self.init_deck())
        ui.run()


def main():
    gui = blackjackGui()
    gui.create_ui()
    

    


main()