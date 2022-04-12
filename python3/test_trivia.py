from trivia import Game, Player

#A game consists of several players
#Each player has a name, a square placement, a coin purse, an active status and a penalty status
#Each game has a number of players, a set of questions in 4 categories, and a state machine with rules.

#State machine:
#   1.      roll dice
#   2.      branch on penalty box or not
#   2.1     if in penalty box then check if we get out
#   2.1.1   if not getting out, then next player -> 6
#   2.1.2   if getting out, continue to move
#   3.      move square depending on roll
#   4.      Ask question
#   5.      Branch on answer
#   5.1     if wrong put player in penalty box, then next player -> 6 
#   5.2     if correct give player coin and check winning condition
#   6.      give turn to next player



def setup():
    game = Game()
    names = ["Suzy", "David", "Juan"]
    for name in names:
        game.add_player(name)
    return game, names

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
    for player in game.players_new.values():
        _verify_player_added(player, player.name)

def test_current_player_is_initialized_to_first_added():
    game, names = setup()
    assert game.current_player_new.name == names[0]
    print(names[0])

def test_next_turn_changes_active_player():
    game, names = setup()
    for name in names:
        assert game.current_player_new.name == name
        game.give_turn_to_next_player()
    assert game.current_player_new.name == names[0]

def test_player_moves_correctly():
    game, names = setup()
    test_player = game.players_new[names[0]]
    dice_roll_1 = 3
    game.move_player(test_player, dice_roll_1)
    assert test_player.square == dice_roll_1
    dice_roll_2 = 6
    game.move_player(test_player, dice_roll_2)
    assert test_player.square == dice_roll_1 + dice_roll_2
    dice_roll_3 = 4
    game.move_player(test_player, dice_roll_3)
    assert test_player.square == 1

def test_correct_category_is_displayed():
    game, names = setup()
    test_player = game.players_new[names[0]]
    test_player.square = 0
    assert game._current_category_new == 'Pop'
    test_player.square = 1
    assert game._current_category_new == 'Science'
    test_player.square = 2
    assert game._current_category_new == 'Sports'
    test_player.square = 7
    assert game._current_category_new == 'Rock'

def test_case_put_player_in_penalty_box():
    game, names = setup()
    dice_roll = 1
    correct_answer = False
    game.play_turn(dice_roll, correct_answer)
    assert game.players_new[names[0]].penalty == True



# def test_penalty_box_has_correct_logic():
#     game, names = setup()
    


# def test_case_player_stays_in_penalty_box():
#     roll
