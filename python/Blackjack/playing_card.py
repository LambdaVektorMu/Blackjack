from enum import Enum, auto, IntEnum, unique
from typing import List
import random

# トランプの絵柄
@unique
class Suit(Enum):
    CLUB = auto()
    DIAMOND = auto()
    HEART = auto()
    SPADE = auto()

# トランプの数値
@unique
class Number(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

# トランプ1枚のクラス
class Card():
    def __init__(self, suit: Suit, number: Number) -> None:
        self.suit = suit
        self.number = number

    def get_suit(self) -> Suit:
        return self.suit

    def get_number(self) -> Number:
        return self.number

# トランプの山札クラス
# 13種*4スートの重複無し52枚
# 山札の順番はカードリストのインデックスの昇順（インデックス0が頂上）
class Deck():
    # 山札を作成する
    def __init__(self) -> None:
        self.cards: List[Card] = []
        for s in Suit:
            for no in Number:
                self.cards.append(Card(s, no))

    # 山札の残り枚数を返す
    def count_remainder(self) -> int:
        return len(self.cards)

    # 山札をランダムに並べ替える
    def shuffle_cards(self) -> None:
        random.shuffle(self.cards)

    # 山札の頂上から1枚カードを引く
    def draw_card(self) -> Card:
        return self.cards.pop(0)
