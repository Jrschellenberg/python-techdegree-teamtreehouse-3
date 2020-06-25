import os
from phrasehunter.character import Character


class Phrase(list):
    def __init__(self, phrase):
        super().__init__()
        for char in phrase:
            self.append(Character(char))
        if os.environ.get('DEBUG', False):
            print(f"DEUBGMODE: Phrase = {phrase}")

    def __str__(self):
        string = ""
        for char in self:
            string += char.character
        return string

    def is_phrase_guessed(self):
        for char in self:
            if not char.guessed:
                return False
        return True

    def player_guess(self, guessed_char):
        keep_live = False
        for char in self:
            if char.validate_guess(guessed_char):
                keep_live = True
        return keep_live
