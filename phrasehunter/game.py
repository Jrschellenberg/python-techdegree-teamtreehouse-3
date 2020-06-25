import sys
import re
from phrasehunter.phrase import Phrase
from random import randint


class Game:
    def __init__(self, phrases=[], lives=5):
        self._player_guesses = []
        self._lives = lives
        self.phrases = phrases
        self._phrase = None

    @property
    def phrase(self):
        return self._phrase

    @phrase.setter
    def phrase(self, value):
        self._phrase = Phrase(value)

    def _get_player_guesses(self):
        string = ""
        for guess in self._player_guesses:
            string += f', {guess}'
        return string.replace(', ', '', 1)

    def _is_still_alive(self):
        return 0 < self._lives

    def _guess_character(self):
        while True:
            try:
                print(f"You have Guessed the following letters [ {self._get_player_guesses()} ]")
                player_guess = input("Please guess a letter, or 1 to quit:  ")
                if player_guess == '1':
                    sys.exit(0)
                if not len(player_guess) == 1:
                    raise ValueError("Please enter 1 character only!")
                if re.match(r'[A-z]', player_guess) is None:
                    raise ValueError("Need to guess an english alphabet uppercase, or lowercase Letter!")
                if player_guess.lower() in self._player_guesses:
                    raise ValueError(f"You have already guessed {player_guess}, Please guess another Letter!")
                break
            except ValueError as e:
                print(f'\n{e}\n')
        keep_life = self.phrase.player_guess(player_guess)
        self._player_guesses.append(player_guess.lower())
        if not keep_life:
            self._lives -= 1

    def start_game(self):
        while self._is_still_alive():
            print(str(self.phrase))
            print(f'You have {self._lives} lives remaining')
            self._guess_character()
            if self.phrase.is_phrase_guessed():
                break
        if self._is_still_alive():
            print(f"You won! while maintaining {self._lives} lives! Congrats!")
        else:
            print("Sorry, you lost :(")

    def initialize_game(self, lives=5):
        phrase = self.phrases.pop(randint(0, len(self.phrases) - 1))
        self.phrase = phrase
        self._lives = lives
        self._player_guesses = []
