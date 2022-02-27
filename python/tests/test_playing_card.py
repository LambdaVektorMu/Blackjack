from cgi import print_directory
from Blackjack.playing_card import Deck

def print_Deck(deck: Deck) -> None:
    print(len(deck.cards))
    for card in deck.cards:
        print(card.get_suit().name, card.get_number().name, card.get_number().value)


def test_Deck():
    deck = Deck()
    print_Deck(deck)

    while deck.count_remainder() > 0:
        print(deck.count_remainder())
        card = deck.draw_card()
        print(card.get_suit().name, card.get_number().value)

    deck = Deck()
    print("shuffle deck")
    deck.shuffle_cards()
    print_Deck(deck)
