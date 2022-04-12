class Player:
    def __init__(self, name):
        self.name = name
        self.square = 0
        self.coins = 0
        self.penalty = False
        self.active = False

class Game:
    def __init__(self):
        self.players = dict()
        self.winner = ""

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = None

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)
    
        
    @property
    def _current_category(self):
        if self.current_player.square in [0, 4, 8]: return 'Pop'
        if self.current_player.square in [1, 5, 9]: return 'Science'
        if self.current_player.square in [2, 6, 10]: return 'Sports'
        return 'Rock'

    def add_player(self, name):
        self.players[name] = Player(name)
        if len(self.players) == 1: 
            self.current_player = self.players[name]
        print(f"{name} was added")
        print(f"They are player number {len(self.players)}")

    def play_turn(self, player, dice_roll, simulated_answer=None):
        print(f"{player.name} is the current player")
        print(f"They have rolled a {dice_roll}")
        if(self.check_penalty(player, dice_roll)):
            self.give_turn_to_next_player()
            return
        self.move_player(player, dice_roll)
        answer = self.ask_question(simulated_answer)
        if answer is True:
            print('Answer was correct!!!!')
            self.award_coin(player)
            if self.check_winning_condition() is True:
                return False
        else:
            print('Question was incorrectly answered')
            self.put_player_in_penalty(player)
        self.give_turn_to_next_player()
        return True

    def give_turn_to_next_player(self):
        list_of_players = list(self.players.keys())
        current_player_name = self.current_player.name
        index_of_current_player = list_of_players.index(current_player_name)

        index_of_next_player = index_of_current_player + 1
        if index_of_next_player >= len(list_of_players):
            index_of_next_player = 0

        next_player_name = list_of_players[index_of_next_player]
        self.current_player = self.players[next_player_name]

    def move_player(self, player, dice_roll):
        player.square += dice_roll
        if player.square > 11:
            player.square -= 12
        print(f'{player.name}\'s new location is {player.square}')
    
    def check_penalty(self, player, dice_roll):
        if player.penalty is True:
            if dice_roll%2 == 0:
                print(f"{player.name} stays in the penalty box")
                return True
            else:
                self.remove_player_from_penalty(player)
        return False

    def award_coin(self, player):
        player.coins += 1
        print(f'{player.name} now has {player.coins} Gold Coins.')

    def check_winning_condition(self):
        for player in self.players.values():
            if player.coins == 6:
                self.winner = player.name
                return True
        return False
                
    def ask_question(self, simulated_answer=None):
        self.display_question()
        answer = simulated_answer
        if answer == None:
            while (answer != False or answer != True):
                print("Please write \"True\" or \"False\": \n")
                answer = input()
        return answer

    def display_question(self):
        print(f"The category is {self._current_category}")
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    def put_player_in_penalty(self, player):
        print(f"{player.name} was sent to the penalty box")
        player.penalty = True

    def remove_player_from_penalty(self, player):
        print(f"{player.name} is getting out of the penalty box")
        player.penalty = False

