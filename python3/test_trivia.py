from trivia_new import Game as Game_new, Player
from trivia import Game

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
    game = Game_new()
    names = ["Chet", "Pat", "Sue"]
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
    game = Game_new()
    names = ["Suzy", "David", "Juan"]
    for name in names:
        game.add_player(name)
    assert len(game.players) == len(names)
    for player in game.players.values():
        _verify_player_added(player, player.name)

def test_current_player_is_initialized_to_first_added():
    game, names = setup()
    assert game.current_player.name == names[0]
    print(names[0])

def test_next_turn_changes_active_player():
    game, names = setup()
    for name in names:
        assert game.current_player.name == name
        game.give_turn_to_next_player()
    assert game.current_player.name == names[0]

def test_player_moves_correctly():
    game, names = setup()
    test_player = game.players[names[0]]
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
    test_player = game.players[names[0]]
    test_player.square = 0
    assert game._current_category == 'Pop'
    test_player.square = 1
    assert game._current_category == 'Science'
    test_player.square = 2
    assert game._current_category == 'Sports'
    test_player.square = 7
    assert game._current_category == 'Rock'

def test_case_put_player_in_penalty_box():
    game, names = setup()
    dice_roll = 1
    simulated_answer = False
    player = game.current_player
    game.play_turn(player, dice_roll, simulated_answer)
    assert player.penalty == True
    return game, player

def test_case_release_player_from_penalty_box():
    game, player = test_case_put_player_in_penalty_box()
    dice_roll = 1
    simulated_answer = True
    game.play_turn(player, dice_roll, simulated_answer)
    assert player.penalty == False
    return game, player

def test_case_player_gets_coin_for_correct_answer():
    game, player = test_case_release_player_from_penalty_box()
    assert player.coins == 1

def test_case_player_wins():
    game, names = setup()
    player = game.current_player
    player.coins = 5
    dice_roll = 1
    simulated_answer = True
    game.play_turn(player, dice_roll, simulated_answer)
    assert game.winner == player.name

def test_compare_old_and_new_code():
    from random import randrange
    not_a_winner = False
    not_a_winner_new = False
    game = Game()
    game_new = Game_new()

    names = ["Chet", "Pat", "Sue"]
    for name in names:
        game.add(name)
        game_new.add_player(name)


    while True:
        player = game_new.current_player
        roll = randrange(5) + 1
        game.roll(roll)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
            not_a_winner_new = game_new.play_turn(player, roll, simulated_answer=False)
            
        else:
            not_a_winner = game.was_correctly_answered()
            not_a_winner_new = game_new.play_turn(player, roll, simulated_answer=True)

        if not not_a_winner:
            print(not_a_winner)
            print("old")
            break
    
        # if not not_a_winner_new:
        #     print("new")
        #     break
    print(game.places)
    print(game.purses)

    for i, player in enumerate(game.players):
        print(f"{player}: Square {game.places[i]}, Coins {game.purses[i]}")
        player_new = game_new.players[player]
        print(f"{player_new.name}: Square {player_new.square}, Coins {player_new.coins}")
        assert game.places[i] == player_new.square
        assert game.purses[i] == player_new.coins
    