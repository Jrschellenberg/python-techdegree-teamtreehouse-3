import re


class Character:
    placeholder_char = '_'

    def __init__(self, char):
        if len(char) != 1:
            raise ValueError('Character class may only take character of 1 length!')
        self._character = char
        self._guessed = char == ' '

    @property
    def character(self):
        return self._character if self._guessed else Character.placeholder_char

    @property
    def guessed(self):
        return self._guessed

    @guessed.setter
    def guessed(self, value):
        self._guessed = value

    @character.setter
    def character(self, value):
        self._character = value

    def validate_guess(self, guessed_char):
        if re.match(self._character, guessed_char, re.IGNORECASE) is not None:
            self._guessed = True
            return True
        return False
