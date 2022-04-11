from trivia import Game

def setup():
    game = Game()
    return game

def inc(x):
    return x + 1


def test_answer():
    game = setup()
    print(game.players)
    assert inc(3) == 5