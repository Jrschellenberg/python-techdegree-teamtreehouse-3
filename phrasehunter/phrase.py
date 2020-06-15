from random import randint


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
    def __init__(self):
        phrase = RANDOM_PHRASES[randint(0, len(RANDOM_PHRASES)-1)]
        print(phrase)
