#!/usr/bin/env python3

from gettext import find
from itertools import cycle
class Player:
    def __init__(self, name):
        self.name = name
        self.square = 0
        self.coins = 0
        self.penalty = False
        self.active = False
class Game:
    def __init__(self):
        self.players_new = dict()
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player_new = None
        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self):
        return self.how_many_players >= 2

    def add_player(self, name):
        self.players_new[name] = Player(name)
        if len(self.players_new) == 1: 
            self.current_player_new = self.players_new[name]
        print("%s was added", name)
        print("They are player number %s", len(self.players_new))

    def give_turn_to_next_player(self):
        list_of_players = list(self.players_new.keys())
        current_player_name = self.current_player_new.name
        index_of_current_player = list_of_players.index(current_player_name)

        index_of_next_player = index_of_current_player + 1
        if index_of_next_player >= len(list_of_players):
            index_of_next_player = 0

        next_player_name = list_of_players[index_of_next_player]
        self.current_player_new = self.players_new[next_player_name]

    def move_player(self, player, dice_roll):
        player.square += dice_roll
        if player.square > 11:
            player.square -= 12
        print('%s\'s new location is %s', player.name, player.square)
    
    def check_penalty(self, player, dice_roll):
        if player.penalty is True:
            if dice_roll%2 != 0:
                print("%s stays in the penalty box", player.name)
                return True
            else:
                self.remove_player_from_penalty(player)
        return False

    def award_coin(self, player):
        player.coins += 1

    def ask_question_new(self, simulated_answer=None):
        self.display_question()
        answer = simulated_answer
        if answer == None:
            while (answer != False or answer != True):
                print("Please write \"True\" or \"False\": \n")
                answer = input()
        return answer

    def display_question(self):
        print("The category is %s", self._current_category_new)
        if self._current_category_new == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category_new == 'Science': print(self.science_questions.pop(0))
        if self._current_category_new == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category_new == 'Rock': print(self.rock_questions.pop(0))

    def put_player_in_penalty(self, player):
        print("%s was sent to the penalty box", player.name)
        player.penalty = True

    def remove_player_from_penalty(self, player):
        print("%s is getting out of the penalty box", player.name)
        player.penalty = False

    def play_turn(self, player, dice_roll, simulated_answer=None):
        print("%s is the current player", player.name)
        print("They have rolled a %s", dice_roll)
        if(self.check_penalty(player, dice_roll)):
            return
        self.move_player(player, dice_roll)
        answer = self.ask_question_new(simulated_answer)
        if answer is True:
            self.award_coin(player)
        else:
            self.put_player_in_penalty(player)
        self.give_turn_to_next_player()
        return

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'
    
    @property
    def _current_category_new(self):
        if self.current_player_new.square in [0, 4, 8]: return 'Pop'
        if self.current_player_new.square in [1, 5, 9]: return 'Science'
        if self.current_player_new.square in [2, 6, 10]: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
