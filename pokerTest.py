import unittest
from hamcrest import *

from card import Card
from sessions import InputValidation


class PokerTest(unittest.TestCase):

    def setUp(self):
        self.inputValidator = InputValidation()

    ##### VALIDATION TESTS ######

    def testEmptyString(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("",""), raises(ValueError, "Invalid"))

    def testTooManyCardsForBlack(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2S 3H 4S 6H 7S 8D","2H 3S 4H 6S 7H"), raises(ValueError, "Invalid"))

    def testTooManyCardsForWhite(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2H 3S 4H 6S 7H", "2S 3H 4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    def testTooManyCardsForBoth(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2H 3S 4H 6S 7H 9D", "2S 3H 4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    def testNotEnoughCardsForBlack(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2S 3H 4S 6H","2H 3S 4H 6S 7H"), raises(ValueError, "Invalid"))

    def testNotEnoughCardsForWhite(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2H 3S 4H 6S 7H", "4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    def testNotEnoughCardsForBoth(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2H 3S 4H 6S", "4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    def testForRepeatedCardsForBlack(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2H 3S 4H 6S 6S", "TS 4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    def testForRepeatedCardsForWhite(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2H 3S 4H 6S TS", "6H 4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    def testForRepeatedCardsForBoth(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2H 3S 4H AS TS", "TS 4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    def testForMoreThenTwoEnteries(self):
        assert_that(calling(self.inputValidator.isCardsValid).with_args("2HS 3S 4H AS JS", "TS 4S 6H 7S 8D"), raises(ValueError, "Invalid"))

    ##### CARD TESTS ######

    def testCardsNumeral(self):
        assert_that(Card("2", "S").numeral, is_(2))

    def testCardsSuits(self):
        assert_that(Card("2", "S").suit, is_("S"))

    def testCardsWrongNumeral(self):
        assert_that(calling(Card).with_args("0", "S"), raises(ValueError, "Wrong Numeral"))

    def testCardsWrongNumeral(self):
        assert_that(calling(Card).with_args("2", "F"), raises(ValueError, "Wrong Suit"))



#DO NOT TOUCH
if __name__ == '__main__':
    unittest.main()