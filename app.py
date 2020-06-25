import sys
from phrasehunter.game import Game


# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop


def init():
    try:
        game = Game()
        game.start_game()
    except ValueError as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    init()
