from typing import List
from Blackjack.playing_card import Deck, Card
from Blackjack.playing_card import Suit, Number

def test_Card():
    for s in Suit:
        for n in Number:
            card = Card(s, n)
            assert card.get_number() == n
            assert card.get_suit() == s


def print_Deck(deck: Deck) -> None:
    print(len(deck.cards))
    for card in deck.cards:
        print(card.get_suit().name, card.get_number().name, card.get_number().value)


def test_Deck():
    # テスト対象
    deck = Deck()
    # テスト用インスタンス
    cards: List[Card] = []
    for s in Suit:
        for n in Number:
            cards.append(Card(s, n))
    counter = 52

    print_Deck(deck)
    assert deck.count_remainder() == counter

    for i in range(52):
        counter -= 1
        print(deck.count_remainder())
        card = deck.draw_card()
        print(card.get_suit().name, card.get_number().value)
        assert deck.count_remainder() == counter
        assert card.get_suit() == cards[i].get_suit()
        assert card.get_number() == cards[i].get_number()

    deck = Deck()
    print("shuffle deck")
    deck.shuffle_cards()
    print_Deck(deck)
