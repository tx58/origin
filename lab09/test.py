"""
A unit test for module blackjack

Run this test script to make sure everything is working properly.

Authors: L. Lee (LJL2), S. Marschner (SRM2), and W. White (WMW2)
Date:   October 24, 2018
"""
import introcs
import card
import bjack


def test_game_init():
    """
    Tests the __init__ method for Blackjack objects
    """
    c1 = card.Card(0, 12)
    c2 = card.Card(1, 10)
    c3 = card.Card(2, 9)
    c4 = card.Card(0, 1)

    # Initialize deck and start game.
    deck = [c1, c2, c3, c4]
    game = bjack.Blackjack(deck)

    introcs.assert_equals([c1, c2], game.playerHand)
    introcs.assert_equals([c3], game.dealerHand)
    introcs.assert_equals([c4], deck)  # check that cards were removed

    deck = card.Card.deck()  # non-shuffled deck
    game = bjack.Blackjack(deck)
    c1 = card.Card(0, 1)
    c2 = card.Card(0, 2)
    c3 = card.Card(0, 3)
    c4 = card.Card(0, 4)

    introcs.assert_equals([c1, c2], game.playerHand)
    introcs.assert_equals([c3], game.dealerHand)

    # check that right cards were removed
    introcs.assert_equals(card.Card.deck()[3:], deck)

    print('The blackjack __init__ tests passed')


def test_game_str():
    """
    Tests the __str__ function for Blackjack objects
    """
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)
    introcs.assert_equals('player: 20; dealer: 9', str(game))

    game.playerHand=[]
    introcs.assert_equals('player: 0; dealer: 9', str(game))
    game.dealerHand.append(card.Card(2,1))
    introcs.assert_equals('player: 0; dealer: 20', str(game))
    game.dealerHand.append(card.Card(2,5))
    introcs.assert_equals('player: 0; dealer: 25', str(game))

    print('The blackjack __str__ tests passed')


def test_game_score():
    """
    Tests the _score method (which is hidden, but we access anyway)
    """
    # need a dummy game object to call its _score function (and test it)
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_equals(13, game._score([card.Card(2, 2), card.Card(3, 1)]))
    introcs.assert_equals(13, game._score([card.Card(1, 13), card.Card(0, 3)]))
    introcs.assert_equals(22, game._score([card.Card(1, 1), card.Card(0, 1)]))
    introcs.assert_equals(9, game._score([card.Card(1, 2), card.Card(0, 3), card.Card(3, 4)]))
    introcs.assert_equals(0, game._score([]))

    print('The blackjack _score tests passed')


def test_dealerScore():
    """
    Tests the dealerScore method for Blackjack objects
    """
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_equals(9, game.dealerScore())
    game.dealerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.playerHand = [card.Card(1, 13), card.Card(0, 3)]
    introcs.assert_equals(13, game.dealerScore())

    print('The dealerScore tests passed')


def test_playerScore():
    """
    Tests the playerScore method for Blackjack objects
    """
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_equals(20, game.playerScore())
    game.playerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.dealerHand = [card.Card(1, 13), card.Card(0, 3)]
    introcs.assert_equals(13, game.playerScore())

    print('The playerScore tests passed')


def test_playerBust():
    """
    Tests the playerBust method for Blackjack objects
    """
    # get dummy deck
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = bjack.Blackjack(deck)

    introcs.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10)]
    introcs.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    introcs.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    introcs.assert_true(game.playerBust())

    print('The playerBust tests passed')


def test_dealerBust():
    """
    Tests the dealerBust method for Blackjack objects
    """
    # get dummy deck
    deck = [card.Card(0, 12),  card.Card(2, 9), card.Card(1, 10),]
    game = bjack.Blackjack(deck)

    introcs.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10)]
    introcs.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    introcs.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    introcs.assert_true(game.dealerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    introcs.assert_true(game.playerBust())

    print('The dealerBust tests passed')


def test_wild_setters():
    """
    Tests the setters for the WildCard objects

    This test does not require that the initializer work yet.  If you still
    have pass in the initilizer, these tests should be fine.

    This test does not require that setCode support the 'WC' code.  This is
    an optional exercise.
    """
    import wild
    
    # This will create an empty card if the initializer is not defined
    card = wild.WildCard()

    card.setSuit(1)
    introcs.assert_equals(1,card.getSuit())
    card.setRank(3)
    introcs.assert_equals(3,card.getRank())

    card.setWild(True)
    introcs.assert_true(card.isWild())
    card.setWild(False)
    introcs.assert_false(card.isWild())

    try:
        card.setWild(5)
        introcs.quit_with_error('setWild does not enforce preconditions')
    except:
        pass

    # Check that setCode works on codes OTHER than 'WC'
    card.setCode('AS')
    introcs.assert_equals(1,card.getRank())
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals('AS',card.getCode())

    print('The wild setter tests passed')


def test_wild_init():
    """
    Tests the initializer for the WildCard objects

    This test does not require that setCode support the 'WC' code.  This is
    an optional exercise.
    """
    import wild
    
    # This will create an empty card if the initializer is not defined
    card = wild.WildCard(1,12)
    introcs.assert_equals(1,card.getSuit())
    introcs.assert_equals(12,card.getRank())
    introcs.assert_equals('QD',card.getCode())
    introcs.assert_false(card.isWild())

    card = wild.WildCard(2,11,True)
    introcs.assert_equals(2,card.getSuit())
    introcs.assert_equals(11,card.getRank())
    introcs.assert_true(card.isWild())

    card = wild.WildCard(2,11,True,'AS')
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals(1,card.getRank())
    introcs.assert_false(card.isWild())

    try:
        card = wild.WildCard(5,11,True)
        introcs.quit_with_error('initializer does not enforce preconditions')
    except:
        pass

    try:
        card = wild.WildCard(2,0,True)
        introcs.quit_with_error('initializer does not enforce preconditions')
    except:
        pass

    try:
        card = wild.WildCard(2,11,3)
        introcs.quit_with_error('initializer does not enforce preconditions')
    except:
        pass

    print('The wild __init__ tests passed')


def test_wild_str():
    """
    Tests that __str__ works properly for WildCard.
    """
    import wild
    
    card = wild.WildCard(1,12)
    introcs.assert_equals('Queen of Diamonds',str(card))
    card = wild.WildCard(0,3)
    introcs.assert_equals('3 of Clubs',str(card))
    card = wild.WildCard(3,1,True)
    introcs.assert_equals('Ace of Spades [WILD]',str(card))
    card = wild.WildCard(1,12,True)
    introcs.assert_equals('Queen of Diamonds [WILD]',str(card))
    card = wild.WildCard(0,3,True)
    introcs.assert_equals('3 of Clubs [WILD]',str(card))


# OPTIONAL EXERCISES
def test_wild_code():
    """
    Tests that setCode (and the initializer) works properly for WildCard.
    """
    import wild
    
    # This will create an empty card if the initializer is not defined
    card = wild.WildCard()
    card.setCode('QD')
    introcs.assert_equals(1,card.getSuit())
    introcs.assert_equals(12,card.getRank())
    introcs.assert_equals('QD',card.getCode())
    introcs.assert_false(card.isWild())

    card.setCode('WC')
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals(1,card.getRank())
    introcs.assert_equals('WC',card.getCode())
    introcs.assert_true(card.isWild())

    try:
        card.setCode(23)
        introcs.quit_with_error('setCode does not enforce preconditions')
    except:
        pass

    try:
        card.setCode('WD')
        introcs.quit_with_error('setCode does not enforce preconditions')
    except:
        pass

    card = wild.WildCard(code='QD')
    introcs.assert_equals(1,card.getSuit())
    introcs.assert_equals(12,card.getRank())
    introcs.assert_equals('QD',card.getCode())
    introcs.assert_false(card.isWild())

    card = wild.WildCard(code='WC')
    introcs.assert_equals(3,card.getSuit())
    introcs.assert_equals(1,card.getRank())
    introcs.assert_equals('WC',card.getCode())
    introcs.assert_true(card.isWild())

    card = wild.WildCard(2,11,True)
    introcs.assert_equals(2,card.getSuit())
    introcs.assert_equals(11,card.getRank())
    introcs.assert_equals('WC',card.getCode())
    introcs.assert_true(card.isWild())

    print('The wild setCode tests passed')


def test_wild_eq():
    """
    Tests that __eq__ works properly for WildCard.
    """
    import wild
    
    card1 = wild.WildCard(1,12,False)
    card2 = card.Card(1,12)
    introcs.assert_equals(card1,card1)
    introcs.assert_not_equals(card1,card2)

    card2 = wild.WildCard(1,12)
    introcs.assert_equals(card1,card1)

    card2 = wild.WildCard(1,12,True)
    introcs.assert_not_equals(card1,card2)
    card2 = wild.WildCard(3,12)
    introcs.assert_not_equals(card1,card2)
    card2 = wild.WildCard(1,1)
    introcs.assert_not_equals(card1,card2)

    print('The wild __eq__ tests passed')

def test_wild_lt():
    """
    Tests that __lt__ works properly for WildCard.
    """
    import wild
    
    card1 = wild.WildCard(code='QD')
    card2 = wild.WildCard(code='QS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card1 = wild.WildCard(code='JD')
    card2 = wild.WildCard(code='QD')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card1 = wild.WildCard(code='2C')
    card2 = wild.WildCard(code='AS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card3 = wild.WildCard(code='WC')
    introcs.assert_true(card3<card2)
    introcs.assert_false(card2<card3)
    introcs.assert_true(card1<card3)
    introcs.assert_false(card3<card1)

    print('The wild __lt__ tests passed')


def test_wild_deck():
    """
    Tests that the classmethod deck works properly for WildCard.
    """
    import wild
    
    deck1 = card.Card.deck()
    deck2 = wild.WildCard.deck()

    introcs.assert_equals(len(deck1)+2,len(deck2))
    for pos in range(len(deck1)):
        introcs.assert_equals(deck1[pos].getSuit(),deck2[pos].getSuit())
        introcs.assert_equals(deck1[pos].getRank(),deck2[pos].getRank())
        introcs.assert_false(deck2[pos].isWild())

    rdjoker = deck2[-2]
    introcs.assert_equals(2,rdjoker.getSuit())
    introcs.assert_equals(1,rdjoker.getRank())
    introcs.assert_true(rdjoker.isWild())

    bkjoker = deck2[-1]
    introcs.assert_equals(3,bkjoker.getSuit())
    introcs.assert_equals(1,bkjoker.getRank())
    introcs.assert_true(bkjoker.isWild())

    print('The wild deck tests passed')


# Script code
if __name__ == '__main__':
    test_game_init()
    test_game_score()
    test_dealerScore()
    test_playerScore()
    test_dealerBust()
    test_playerBust()
    test_game_str()

    test_wild_setters()
    test_wild_init()
    test_wild_str()

    # OPTIONALS.  UNCOMMENT ALL YOU DO
    #test_wild_code()
    #test_wild_eq()
    #test_wild_lt()
    #test_wild_deck()

    print('All tests for lab 9 passed')
