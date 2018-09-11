from card import Card

suit_list = ('C', 'D', 'H', 'S')
numeral_list = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
#
# class PokerCards:
#     def __init__(self, suit, numeral):
#         self.suit = suit
#         self.numeral = numeral
#     def __repr__(self):
#         return 'pokerCards(suit=%s, numeral=%s' % (self.suit, self.numeral)
# class PokerHands:
#     def __init__(self, listOfCards):
#         self.listOfCards = listOfCards
#
class InputValidation:

    def isCardsValid(self, hand1, hand2):
        knownValue = []
        for cards in [hand1.split(), hand2.split()]:
            if not len(cards) == 5:
                raise ValueError("Invalid")
            for card in cards:
                if (not len(card) == 2) or card in knownValue:
                    raise ValueError("Invalid")
                else:
                    Card(card[0], card[1])
                    knownValue.append(card)
        return True








