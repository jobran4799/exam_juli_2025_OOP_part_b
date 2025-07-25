from enum import Enum, auto
import random
import copy
from abc import ABC, abstractmethod


class DeckCheatingError(Exception):
    pass


class CardSuit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class CardRank(Enum):
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
    ACE = 14


class AbstractCard(ABC):
    @property
    @abstractmethod
    def suit(self): pass

    @property
    @abstractmethod
    def rank(self): pass

    @abstractmethod
    def Get_Display_Name(self): pass


class Card(AbstractCard):
    def __init__(self, suit: CardSuit, rank: CardRank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def Get_Display_Name(self):
        return f'{self.suit.name.capitalize()} OF {self.rank.name.capitalize()}'

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        if self.rank.value < other.rank.value:
            return True
        elif self.rank.value > other.rank.value:
            return False
        elif self.suit.value < other.suit.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.rank.value > other.rank.value:
            return True
        elif self.rank.value < other.rank.value:
            return False
        elif self.suit.value > other.suit.value:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __str__(self):
        return self.Get_Display_Name()

    def __repr__(self):
        return f"Card({self.rank.name}, {self.suit.name})"


class AbstractDeck(ABC):
    @property
    @abstractmethod
    def cards(self): pass

    @abstractmethod
    def shuffle(self): pass

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def add_card(self, card): pass



class Deck(AbstractDeck):

    def __init__(self, shuffle=True):
        self._cards = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        return self._cards[:]

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            out = self._cards[0]
            self._cards.remove(self._cards[0])
            return out
        return None

    def add_card(self, card):
        if card in self._cards:
            raise DeckCheatingError("Card is in deck.")
        self._cards.append(card)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        if len(self._cards) > index:
            return self._cards[index]
        return -1

    def __iter__(self):
        return iter(self._cards)

def create_shuffled_deck():
    return Deck(shuffle=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deck = create_shuffled_deck()
    print(deck.cards[:5])
    drawn_card = deck.draw()
    print(drawn_card)
    deck.add_card(drawn_card)


    print("\nAccessing cards directly by index:")
    for i in range(5):
        print(f"Card at index {i}: {deck[i]}")

    print("\nIterating through all cards in the deck:")
    for card in deck:
        print(card)

