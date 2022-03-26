# ブラックジャックのプレイヤーのモジュール

from Blackjack.playing_card import Card, Deck
from Blackjack.playing_card import Number, Suit
from typing import List


# ディーラー、プレイヤー共通のクラス
class BasePlayer():
    # 手札を用意しておく
    def __init__(self) -> None:
        self.hands: List[Card] = []     # 手札
        self.sum_hands: int = 0         # 手札の合計点

    # 手札に1枚カードを加える
    def add_card(self, card:Card) -> None:
        self.hands.append(card)
        # 入手したカードが絵柄（J,Q,K）の時は+10
        if (card.get_number() is Number.JACK or
            card.get_number() is Number.QUEEN or
            card.get_number() is Number.KING):
            self.sum_hands += 10
        # 入手したカードがエースなら+1
        elif card.get_number() is Number.ACE:
            self.sum_hands += 1
        # 入手したカードが上記以外ならカードの数値を加える
        else:
            self.sum_hands += card.get_number().value

    # 現在の手札の合計点を返す
    def show_point(self) -> int:
        return self.sum_hands

    # 現在の手札を文字列で返す
    def show_hands(self) -> List[str]:
        hand_list: List[str] = []
        for card in self.hands:
            if card.get_suit() is Suit.CLUB:
                hand_list.append("♣"+str(card.get_number().value))
            elif card.get_suit() is Suit.DIAMOND:
                hand_list.append("◆"+str(card.get_number().value))
            elif card.get_suit() is Suit.HEART:
                hand_list.append("♥"+str(card.get_number().value))
            elif card.get_suit() is Suit.SPADE:
                hand_list.append("♠"+str(card.get_number().value))

        return hand_list

    def is_bust(self) -> bool:
        if self.sum_hands > 21:
            return True
        else:
            return False

# ディーラー（CPU側）
class Dealer(BasePlayer):
    def __init__(self, cards: List[Card]) -> None:
        super().__init__()
        for i in range(2):
            self.add_card(cards[i])

    # バーストするか17点を超えるまでカードを引き続ける
    def play_game(self, deck:Deck) -> None:
        while not self.is_bust() or self.show_point() < 17:
            self.add_card(deck.draw_card())
            print(self.show_hands())

# プレイヤー（実行者側）
class Player(BasePlayer):
    def __init__(self, cards: List[Card]) -> None:
        super().__init__()
        for i in range(2):
            self.add_card(cards[i])

    def is_continued_game(self) -> bool:
        print('ゲームを続けますか？')
        x = input()
        if x == 'y' or x == 'Y':
            return True
        else:
            return False

    # バーストするかカードを引くのを止めるまでカードを引き続ける
    def play_game(self, deck:Deck) -> None:
        while not self.is_bust() or self.is_continued_game():
            self.add_card(deck.draw_card())
            print(self.show_hands())
