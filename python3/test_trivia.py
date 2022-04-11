from trivia import Game, Player

#A game consists of several players
#Each player has a name, a square placement, a coin purse, an active status and a penalty status
#Each game has a number of players, a set of questions in 4 categories, and a state machine with rules.



def setup():
    game = Game()
    return game

def test_player_is_initialized_correctly():
    name = "Suzy"
    player1 = Player(name)
    assert player1.name == name
    assert player1.square == 0
    assert player1.coins == 0
    assert player1.penalty == False
    assert player1.active == False
