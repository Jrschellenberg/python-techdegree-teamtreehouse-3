import sys
from phrasehunter.game import Game


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


def init():
    try:
        game = Game(phrases=RANDOM_PHRASES)
        while len(game.phrases) > 0:
            game.initialize_game()
            print(f"PHRASES LEFT {len(game.phrases)}")
            game.start_game()
            play_again = input("Would you like to play Again, Press Enter to play again, or enter 1 to quit:   ")
            if play_again.lower() == '1':
                break
        print("Thanks for Playing! Please come again soon!")
    except ValueError as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    init()
