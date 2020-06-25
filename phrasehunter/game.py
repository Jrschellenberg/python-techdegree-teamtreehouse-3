from phrasehunter.phrase import Phrase
# Create your Game class logic in here.


class Game:
    def __init__(self):
        self._lives = 5
        self.phrase = Phrase()

    def start_game(self):
        pass

    def is_game_won(self):
        return 0 < self._lives <= 5

    def get_phrase(self):
        return str(self.phrase)
