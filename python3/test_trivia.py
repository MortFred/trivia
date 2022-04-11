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
    _verify_player_added(player1, name)

def _verify_player_added(player, name):
    assert player.name == name
    assert player.square == 0
    assert player.coins == 0
    assert player.penalty == False
    assert player.active == False

def test_players_are_added_to_game():
    game = Game()
    names = ["Suzy", "David", "Juan"]
    for name in names:
        game.add_player(name)
    assert len(game.players_new) == len(names)
    for player in game.players_new:
        _verify_player_added(player, player.name)
