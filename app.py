import sys
from phrasehunter.game import Game


# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop


def init():
    while True:
        try:
            game = Game()
            game.start_game()
            play_again = input("Would you like to play Again, Press Enter to play again, or (Q/q) to quit")
            if play_again.lower() == 'q':
                break
            print("Thanks for Playing! Please come again soon!")
        except ValueError as err:
            print(err)
            sys.exit(1)


if __name__ == '__main__':
    init()
