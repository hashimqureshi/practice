numeralDict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
suits = ('C', 'D', 'H', 'S')

class Card:

    def __init__(self, numeral, suit):
        if numeral not in numeralDict.keys():
            raise ValueError("Wrong Numeral")
        if suit not in suits:
            raise ValueError("Wrong Suit")
        self.numeral = numeralDict[numeral]
        self.suit = suit
