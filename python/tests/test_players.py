from Blackjack.players import BasePlayer, Player
from Blackjack.playing_card import Card
from Blackjack.playing_card import Suit, Number
from typing import List


def test_add_card_BasePlayer():
    cp = BasePlayer()
    assert cp.sum_hands == 0
    assert cp.show_point() == 0

    club_cards:List[Card] = [Card(Suit.CLUB, n) for n in Number]
    sum = 0
    for i in range(1, 10):
        sum += i + 1
        cp.add_card(club_cards[i])
        assert cp.show_point() == sum

    cp.add_card(Card(Suit.DIAMOND, Number.ACE))
    sum += 1
    assert cp.show_point() == sum

    cp.add_card(Card(Suit.SPADE, Number.JACK))
    sum += 10
    assert cp.show_point() == sum

    cp.add_card(Card(Suit.HEART, Number.QUEEN))
    sum += 10
    assert cp.show_point() == sum

    cp.add_card(Card(Suit.HEART, Number.KING))
    sum += 10
    assert cp.show_point() == sum
