class Character:
    placeholder_char = '_'

    def __init__(self, char):
        self._character = char
        self._guessed = False

    @property
    def character(self):
        if self._character == " ":
            return self._character
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
