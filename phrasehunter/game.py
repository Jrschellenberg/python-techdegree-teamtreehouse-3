import re
from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self._lives = 5
        self.phrase = Phrase()

    def start_game(self):
        while self.is_still_alive():
            print(self.get_phrase())
            print(f'You have {self._lives} lives remaining')
            self.guess_character()
            if self.phrase.is_phrase_guessed():
                break
        if self.is_still_alive():
            print("You won!")
        else:
            print("Sorry, you lost :(")

    def guess_character(self):
        while True:
            try:
                player_guess = input("Please guess a letter:  ")
                if not len(player_guess) == 1:
                    raise ValueError("Please enter 1 character only!")
                if re.match(r'[A-z]', player_guess) is None:
                    raise ValueError("Need to guess an english alphabet uppercase, or lowercase Letter!")
                break
            except ValueError as e:
                print(f'\n{e}\n')
        keep_life = self.phrase.player_guess(player_guess)
        if not keep_life:
            self._lives -= 1

    def is_still_alive(self):
        return 0 < self._lives

    def get_phrase(self):
        return str(self.phrase)
