"""
A module providing a class for playing cards

This implementation is adapted from chapter 18 of the course text, _Think Python_,
by Allen B. Downey.

Authors: Steve Marschner (srm2), Lillian Lee (ljl2), and Walker White (wmw2)
Date:   October 24, 2018
"""
from functools import total_ordering  # for implementing comparisons in Python3


# decorator "fills in" missing comparisons, at the cost of speed
@total_ordering
class Card(object):
    """
    A class to represent a standard playing card.

    CLASS ATTRIBUTES:
        _SUIT_NAMES: list of valid suit names [list of str]
        _RANK_NAMES: list of valid int ranks to names [list of str]

    INSTANCE ATTRIBUTES:
        _suit: the suit of this particular card.
               The name of this suit is given by SUIT_NAMES[suit].
               [int in 0..len(_SUIT_NAMES)-1]

        _rank: the rank of this particular card.
               The name of this rank is given by RANK_NAMES[rank].
               [int in 1..len(_RANK_NAMES)-1]

    Hence, if we execute c = Card(0, 12), Card._SUIT_NAMES[c._suit] is 'Clubs'
    and Card._RANK_NAMES[c._rank] is 'Queen' and this card is the Queen of Clubs.

    Note that 0 is not a valid rank.  Do not make a card with this rank.
    """
    # CONSTANTS TO DEFINE CARD SUITS AND RANKS (Stored in Class Folder)
    _SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    # Starts at None so that we can treat RANK_NAMES as a translation table:
    # RANK_NAME[1] is 'Ace', RANK_NAME[13] is 'King', etc.
    _RANK_NAMES = [None, 'Ace', '2', '3', '4', '5', '6', '7',
    '8', '9', '10', 'Jack', 'Queen', 'King']

    # GETTERS AND SETTERS
    def getSuit(self):
        """
        Returns the suit of this card.
        """
        return self._suit

    def setSuit(self,value):
        """
        Sets the suit of this card.

        Parameter value: The new suit value
        Precondition: value is an int in 0..len(_SUIT_NAMES)-1
        """
        assert type(value) == int, 'suit %s is not an int' % repr(value)
        assert 0 <= value and value < len(self._SUIT_NAMES), \
                'suit %d is out of range' % value
        self._suit = value

    def getRank(self):
        """
        Returns the rank of this card.
        """
        return self._rank

    def setRank(self,value):
        """
        Sets the rank of this card.

        Parameter value: The new rank value
        Precondition: value is an int in 1..len(_RANK_NAMES)-1
        """
        assert type(value) == int, 'rank %s is not an int' % repr(value)
        assert 1 <= value and value < len(self._RANK_NAMES), \
                'rank %d is out of range' % value
        self._rank = value

    # This is a DERIVED attribute (it is a combination of suit and rank)
    def getCode(self):
        """
        Returns a two-character code for the card.

        The code is a two-character string whose first character
        represents the rank and the second is the first initial of the
        suit.  Non-number ranks are represented by initials.  So '3H' stands
        for 3 of hearts, and 'KS' stands for king of spades).  We use 'T'
        for Ten.
        """
        suit = 'CDHS'[self._suit]
        rank = ' A23456789TJQK'[self._rank]
        return rank+suit

    def setCode(self,value):
        """
        Sets the rank and suit of this card using a two-character code.

        The code should be a two-character string whose first character
        represents the rank and the second is the first initial of the
        suit.  Non-number ranks are represented by initials.  So '3H' stands
        for 3 of hearts, and 'KS' stands for king of spades).  We use 'T'
        for Ten.

        Parameter value: The code for the new rank and suit
        Precondition: value is a 2-char string with value[0] in 'A23456789TJQK'
        and value[1] in 'CDHS'.
        """
        assert type(value) == str, 'code %s is not a str' % repr(value)
        assert len(value) == 2, 'code %s has the incorrect length' % repr(value)
        assert value[0] in 'A23456789TJQK', 'rank %s is invalid' % repr(value[0])
        assert value[1] in 'CDHS', 'suit %s is invalid' % repr(value[1])

        self._rank = ' A23456789TJQK'.index(value[0])
        self._suit = 'CDHS'.index(value[1])

    def __init__(self, suit=0, rank=1, code=None):
        """
        Initializes a card with the given suit and rank.

        The suits and rank are represented as integers.  Alternatively,
        suit and rank can be encoded together in a two-character string like
        '3H' (3 of hearts) or 'KS' (king of spades).  We use 'T' for Ten.

        Example: if we execute c = Card(0, 12), then this card is the Queen of
        Clubs, since _SUIT_NAMES[c._suit] is 'Clubs' and _RANK_NAMES[c._rank] is
        'Queen'. The same card could be created by Card(code='QC').

        If the code parameter is used, the suit and rank parameters are ignored.

        Parameter suit: the suit encoding (optional)
        Precondition: suit is an int in 0..len(_SUIT_NAMES)-1 (inclusive)

        Parameter rank: the rank encoding (optional)
        Precondition: rank is an int in 1..len(_RANK_NAMES)-1 (inclusive)

        Parameter code: the card encoded as a string (optional)
        Precondition: code is a 2-char string with code[0] in 'A23456789TJQK'
        and code[1] in 'CDHS'.
        """
        # The setters take care of all the asserts
        if not code is None:
            self.setCode(code)
        else:
            self.setRank(rank)
            self.setSuit(suit)

    def __str__(self):
        """
        Returns a readable string representation of this card.

        Example: '2 of Hearts'
        """
        return self._RANK_NAMES[self._rank] + ' of ' + self._SUIT_NAMES[self._suit]

    # THESE ARE ONLY NEEDED FOR THE OPTIONAL EXERCISES
    def __eq__(self, other):
        """
        Returns True if other is an equivalent card; False otherwise

        Parameter other: the value to compare
        Precondition: NONE (other can be anything)
        """
        return (isinstance(other,Card) and self._suit == other._suit
                and self._rank == other._rank)

    def __ne__(self, other):
        """
        Returns False if other is an equivalent card; True otherwise

        Parameter other: the value to compare
        Precondition: NONE (other can be anything)
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Returns True if this card is less than other

        Cards are compared according to poker ordering, with Aces high.

        Parameter other: the value to compare
        Precondition: other is a Card
        """
        if (self._rank == other._rank):
            return self._suit < other._suit
        else:
            left = len(self._RANK_NAMES) if self._rank == 1 else self._rank
            rght = len(self._RANK_NAMES) if other._rank == 1 else other._rank
            return left < rght

    @classmethod
    def deck(cls):
        """
        Returns the list of the standard 52 cards

        This is a CLASS method, as indicated by the decorator above.  It is
        designed to be called by the class name before the period: Card.deck()
        Notice the variable is cls, not self.  It holds the id of the CLASS
        FOLDER, not the object folder.
        """
        output = []  # list of cards so far to be returned
        for suit in range(len(cls._SUIT_NAMES)):
            for rank in range(1,len(cls._RANK_NAMES)):  # skip the None value
                output.append(cls(suit,rank))
        return output
