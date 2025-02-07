from nicegui import ui
from blackjackGame import BlackjackGame


class blackjackGui:
    def __init__(self):
        self.game = BlackjackGame()
        self.deck_count = 1
        self.player_hand = None
        self.dealer_hand = None
        

    def update_deck_count(self, deckCount):
        self.deck_count = deckCount
        self.game.initialize_deck(deckCount)

    def init_deck(self):
        self.game.initialize_deck(self.deck_count)
        self.game.deal_initial()
        self.player_hand.set_value(self.game.player.display_hand())
        self.dealer_hand.set_value(self.game.dealer.display_hand())
        self.game.dealer.calculate_score()
        self.game.player.calculate_score()

    def reset(self):
        self.game.reset()
        self.player_hand.set_value("")
        self.dealer_hand.set_value("")

    def first_turn_check(self):
        
        pass


    def create_ui(self):        
        ui.add_body_html('''
        <style>
            .text-box {
                display: flex;  
                align-items: center;
                justify-content:center;
                font-size: 15px;
                padding: 7px;
                width: 20em;
            }   
        
                         
        </style>
        ''')
        ui.number(label='Decks', value=1, format='%d', on_change=lambda e:  self.update_deck_count(int(e.value)) if e.value and int(e.value) > 0 else None)
        self.player_hand = ui.input(label='Player Hand', value=0,).props("readonly").classes("text-box")
        self.dealer_hand = ui.input(label='Dealer Hand', value=0,).props("readonly").classes('text-box')


        ui.button("Start Game", on_click=lambda: self.init_deck())
        ui.button("Reset Game", on_click=lambda: self.reset())
        ui.run()


def main():
    gui = blackjackGui()
    gui.create_ui()
    

    


main()