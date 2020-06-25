import os
from random import randint
from phrasehunter.character import Character


# https://randomwordgenerator.com/phrase.php
RANDOM_PHRASES = [
    "A Fool and His Money are Soon Parted",
    "Curiosity Killed The Cat",
    "When the Rubber Hits the Road",
    "Give a Man a Fish",
    "Down To The Wire",
    "Raining Cats and Dogs",
    "Tough It Out",
    "On the Same Page",
    "Talk the Talk",
    "Quick and Dirty",
]


class Phrase(list):
    def __init__(self, phrase=RANDOM_PHRASES[randint(0, len(RANDOM_PHRASES)-1)]):
        super().__init__()
        for char in phrase:
            self.append(Character(char))
        if os.environ.get('DEBUG', False):
            print(phrase)

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
