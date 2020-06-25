import sys
from phrasehunter.game import Game


def init():
    while True:
        try:
            game = Game()
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
