# Import your Game class
from phrasehunter.game import Game

# Create your Dunder Main statement.

# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop


def init():
    game = Game()
    for _ in range(5):
        print(game.is_game_won())


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    init()

